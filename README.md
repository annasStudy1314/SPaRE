# SPaRE

**Scattering-prior-guided representation learning for fine-grained SAR vehicle recognition**

[Interface Demo](demo/) | [Data](data/README.md) | [中文说明](README_zh.md)

## Public Preview

This repository currently provides a **documentation and interface demonstration**
for SPaRE. The core implementation is not included in this pre-submission preview.

The public content is limited to:

- A brief project description.
- A schematic input/output example using synthetic metadata.
- Links to the official ATRNet-STAR dataset and ATRBench documentation.

Model internals, training code, proxy-generation algorithms, hyperparameter
recipes, trained weights, and experiment records are **not publicly released**
here. This repository cannot reproduce the paper's experiments, and its example
does not perform SAR recognition.

## Interface Demonstration

```bash
python demo/interface_demo.py
```

The script uses only the Python standard library. It prints an example input
description and an output schema. It does not instantiate a model, load images,
make predictions, or report accuracy. All shapes are illustrative.

Conceptually, the method accepts an individual SAR amplitude chip and produces
vehicle-class scores. See [the interface notes](demo/README.md).

## Data

Dataset access is provided by the original authors:

- [Official ATRNet-STAR project](https://github.com/waterdisappear/ATRNet-STAR)
- [Official ATRBench documentation](https://github.com/waterdisappear/ATRNet-STAR/blob/main/ATRBench/README.md)

This repository does not redistribute dataset files, dataset access credentials,
or third-party model weights. Follow the authors' current access procedures and
terms, and cite their work when using the data.

## Release Scope

This is a limited public preview, **not a full open-source implementation or a
reproduction package**. No complete-code availability or future release date is
promised by this page. Publication and citation information will be added when
a public manuscript record is available.

Only the small public interface script is covered by the MIT license in this
repository. The license grants no rights to unreleased code, third-party data,
checkpoints, or the manuscript.
