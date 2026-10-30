# Interface Demonstration

[Project](../README.md) | [Dataset](https://github.com/waterdisappear/ATRNet-STAR)

This standard-library example validates and displays the input/output metadata
for a single-channel SAR recognition interface. It does not run model inference.

## Run

Use Python 3.9 or later. No package installation or GPU is required.
From the repository root:

```bash
python demo/interface_demo.py
python demo/interface_demo.py --input demo/example_input.json
python demo/interface_demo.py --output interface_description.json
python demo/interface_demo.py --help
```

The default input is resolved relative to the script, so it also works when
launched from another working directory. Explicit paths are resolved relative
to your working directory.

## Example Contract

| Field | Example | Meaning |
| --- | --- | --- |
| `input.kind` | `single_channel_sar_amplitude` | SAR amplitude input |
| `input.shape` | `[1, 1, 128, 128]` | Batch, channel, height, width |
| `input.dtype` | `float32` | Illustrative tensor type |
| `output_schema.class_scores_shape` | `[1, 40]` | Batch and class dimensions |
| `inference_performed` | `false` | Metadata demonstration, not a prediction |

The bundled JSON describes one synthetic input. It contains no image pixels,
predicted scores, class labels, or performance measurements. The dimensions
illustrate the interface; validation is not a claim about model compatibility
with arbitrary input sizes or class counts. The dtype field does not specify
image normalization or dataset preprocessing.

## Validation and Export

The validator checks positive integer dimensions, one input channel, expected
layouts and dtype, matching batch dimensions, and the no-inference flag.
Invalid JSON, missing files, and inconsistent metadata produce an explanatory
error and exit code `2`; successful validation exits with code `0`.

Standard output contains the validated JSON. With `--output`, the same JSON is
also written to the selected file. Its parent directory must already exist.
The output path cannot be the input path; an existing separate output file is
overwritten. This exports an interface description, not recognition results.

## Tests

```bash
python -m unittest discover -s tests -v
```
