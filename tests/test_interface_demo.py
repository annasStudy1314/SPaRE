"""Checks for the public metadata interface; no model dependencies required."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "demo" / "interface_demo.py"
SPEC = importlib.util.spec_from_file_location("interface_demo", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InterfaceTests(unittest.TestCase):
    def setUp(self):
        self.example = json.loads(
            (ROOT / "demo" / "example_input.json").read_text(encoding="utf-8")
        )

    def run_cli(self, *args, cwd=None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            cwd=cwd, capture_output=True, text=True, encoding="utf-8",
        )

    def test_bundled_example(self):
        self.assertEqual(MODULE.validate_description(self.example), self.example)

    def test_reject_non_object(self):
        for value in (None, [], "metadata"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.validate_description(value)

    def test_missing_sections(self):
        for key in self.example:
            example = copy.deepcopy(self.example)
            del example[key]
            with self.subTest(key=key), self.assertRaises(ValueError):
                MODULE.validate_description(example)

    def test_invalid_input_dimensions(self):
        for shape in ([1, 1, 128], [1, 1, 0, 128], [True, 1, 128, 128],
                      [1, 1, 128.0, 128], [1, 1, -1, 128]):
            example = copy.deepcopy(self.example)
            example["input"]["shape"] = shape
            with self.subTest(shape=shape), self.assertRaises(ValueError):
                MODULE.validate_description(example)

    def test_multiple_channels(self):
        self.example["input"]["shape"][1] = 3
        with self.assertRaisesRegex(ValueError, "single-channel"):
            MODULE.validate_description(self.example)

    def test_invalid_contract_fields(self):
        for section, key, value in (
            ("input", "dtype", "uint8"),
            ("input", "layout", "NHWC"),
            ("input", "kind", "optical"),
            ("output_schema", "layout", "class, batch"),
            ("output_schema", "class_scores_shape", [1, 0]),
            ("output_schema", "class_scores_shape", [1]),
        ):
            example = copy.deepcopy(self.example)
            example[section][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                MODULE.validate_description(example)

    def test_batch_mismatch(self):
        self.example["output_schema"]["class_scores_shape"][0] = 2
        with self.assertRaisesRegex(ValueError, "batch"):
            MODULE.validate_description(self.example)

    def test_inference_flag_must_be_false(self):
        for value in (True, 0, "false", None):
            example = copy.deepcopy(self.example)
            example["inference_performed"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.validate_description(example)

    def test_default_cli_from_another_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli(cwd=directory)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), self.example)

    def test_export(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "description.json"
            result = self.run_cli("--output", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")),
                             self.example)
            self.assertEqual(json.loads(result.stdout), self.example)

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "invalid.json"
            source.write_text("{broken", encoding="utf-8")
            result = self.run_cli("--input", source)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_input(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli("--input", Path(directory) / "missing.json")
        self.assertEqual(result.returncode, 2)

    def test_prevent_input_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.json"
            original = json.dumps(self.example)
            source.write_text(original, encoding="utf-8")
            result = self.run_cli("--input", source, "--output", source)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(source.read_text(encoding="utf-8"), original)

    def test_missing_output_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli("--output", Path(directory) / "absent" / "out.json")
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
