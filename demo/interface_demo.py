"""Validate and display SAR interface metadata without performing inference."""

import argparse
import json
from pathlib import Path
from typing import Optional, Sequence


def _shape(value: object, dimensions: int, name: str) -> list:
    if (
        not isinstance(value, list)
        or len(value) != dimensions
        or any(type(item) is not int or item <= 0 for item in value)
    ):
        raise ValueError(f"{name} must contain {dimensions} positive integers")
    return value


def validate_description(description: object) -> dict:
    """Check the demonstration contract, not model or dataset compatibility."""
    if not isinstance(description, dict):
        raise ValueError("the JSON document must be an object")
    if description.get("example_type") != "synthetic_input_description":
        raise ValueError("example_type must be synthetic_input_description")
    if description.get("inference_performed") is not False:
        raise ValueError("inference_performed must be false for this schema demo")

    inputs = description.get("input")
    outputs = description.get("output_schema")
    if not isinstance(inputs, dict) or not isinstance(outputs, dict):
        raise ValueError("input and output_schema must be objects")
    shape = _shape(inputs.get("shape"), 4, "input.shape")
    scores = _shape(outputs.get("class_scores_shape"), 2,
                    "output_schema.class_scores_shape")
    if inputs.get("kind") != "single_channel_sar_amplitude" or shape[1] != 1:
        raise ValueError("input must describe single-channel SAR amplitude")
    if inputs.get("layout") != "batch, channel, height, width":
        raise ValueError("input.layout must be batch, channel, height, width")
    if inputs.get("dtype") != "float32":
        raise ValueError("input.dtype must be float32 in this example")
    if outputs.get("layout") != "batch, class":
        raise ValueError("output_schema.layout must be batch, class")
    if scores[0] != shape[0]:
        raise ValueError("input and output batch dimensions must match")
    return description


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate and display SPaRE interface metadata (no inference)."
    )
    parser.add_argument(
        "--input", type=Path,
        default=Path(__file__).with_name("example_input.json"),
        help="JSON metadata file (default: bundled example)",
    )
    parser.add_argument(
        "--output", type=Path,
        help="also save validated metadata as JSON (parent directory must exist)",
    )
    args = parser.parse_args(argv)
    try:
        if args.output and args.output.resolve() == args.input.resolve():
            raise ValueError("--output must differ from --input")
        description = validate_description(
            json.loads(args.input.read_text(encoding="utf-8"))
        )
        rendered = json.dumps(description, indent=2, ensure_ascii=True) + "\n"
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
