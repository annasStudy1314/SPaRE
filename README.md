# SPaRE

**Scattering-Prior-Aware Representation Enhancement for Fine-Grained SAR Vehicle Recognition**

[Quick Start](#quick-start) | [Interface Guide](demo/README.md) | [Data](https://github.com/waterdisappear/ATRNet-STAR) | [中文说明](README_zh.md)

## Overview

SPaRE studies fine-grained SAR vehicle recognition using single-channel amplitude
images. It connects amplitude-derived scattering priors with task-feature
refinement and local-response organization.

The framework connects three complementary functions:

| Module | Role |
| --- | --- |
| Label-Free Scattering Prior Learning (LSPL) | Learn scattering-related references without category or semantic part labels. |
| Prior-Guided Feature Refinement (PGFR) | Use frozen references to refine task features. |
| Target Component Structure Learning (TCSL) | Organize local responses into component contexts for classification. |

This repository provides a project overview, an input/output interface
demonstration, and links to the official dataset resources.

## Quick Start

**Requirements:** Python 3.9 or later. The interface demo needs no external
packages, GPU, dataset download, or model weights.

Run from the repository root:

```bash
python demo/interface_demo.py
# Export the validated interface description.
python demo/interface_demo.py --output interface_description.json
```

The script validates the bundled example and prints its JSON description.
It demonstrates an interface, not model inference. The example describes a
`[1, 1, 128, 128]` amplitude input and a `[1, 40]` class-score shape; it does not
generate predicted scores or recognition results.

Conceptually, the method accepts an individual SAR amplitude chip and produces
vehicle-class scores. See [the interface notes](demo/README.md).

## Repository Guide

```text
SPaRE/
|-- README.md                  # English project overview
|-- README_zh.md               # Chinese project overview
|-- code/README.md             # Demo entry point
|-- data/README.md             # Official dataset resources
|-- demo/
|   |-- README.md              # Interface specification and usage
|   |-- example_input.json     # Synthetic input/output metadata
|   `-- interface_demo.py      # Validator and JSON export CLI
|-- tests/test_interface_demo.py
`-- LICENSE
```

## Interface Checks

```bash
python -m unittest discover -s tests -v
```

The checks cover metadata validation, command-line execution, JSON export,
invalid inputs, and input-file overwrite protection. They test the public
interface demonstration, not recognition performance.

## Data

Dataset access is provided by the original authors:

- [Official ATRNet-STAR project](https://github.com/waterdisappear/ATRNet-STAR)
- [Official ATRBench documentation](https://github.com/waterdisappear/ATRNet-STAR/blob/main/ATRBench/README.md)

This repository does not redistribute dataset files, dataset access credentials,
or third-party model weights. Follow the authors' current access procedures and
terms, and cite their work when using the data.

## License

The interface example is provided under the [MIT license](LICENSE).
Third-party datasets and other resources remain subject to their respective
licenses and terms.
