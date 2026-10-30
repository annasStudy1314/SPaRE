# SPaRE

**Scattering-Prior-Aware Representation Enhancement for Fine-Grained SAR Vehicle Recognition**

[Interface Demo](demo/) | [Data](https://github.com/waterdisappear/ATRNet-STAR) | [中文说明](README_zh.md)

## Overview

SPaRE studies fine-grained SAR vehicle recognition using single-channel amplitude
images. It connects amplitude-derived scattering priors with task-feature
refinement and local-response organization.

The framework comprises Label-Free Scattering Prior Learning (LSPL),
Prior-Guided Feature Refinement (PGFR), and Target Component Structure Learning
(TCSL). LSPL learns scattering-related references without category or semantic
part labels. PGFR uses the frozen references to refine task features. TCSL
organizes local responses into component contexts for classification.

This repository provides a project overview, an input/output interface
demonstration, and links to the official dataset resources.

## Interface Demonstration

```bash
python demo/interface_demo.py
```

The script uses only the Python standard library. It prints a schematic input
description and output schema to illustrate the interface; it does not run model
inference. All shapes in this example are illustrative.

Conceptually, the method accepts an individual SAR amplitude chip and produces
vehicle-class scores. See [the interface notes](demo/README.md).

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
