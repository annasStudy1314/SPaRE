"""Print a schematic SAR recognition interface; no model inference is performed."""

import json
from pathlib import Path


def main() -> None:
    description = Path(__file__).with_name("example_input.json")
    example = json.loads(description.read_text(encoding="utf-8"))
    print("SPaRE interface preview only. Core implementation is not included.")
    print("The following is a schema, not a recognition result.")
    print(json.dumps(example, indent=2))


if __name__ == "__main__":
    main()
