# Input/Output Interface Preview

This directory demonstrates a possible interface, not the algorithm.

```bash
python demo/interface_demo.py
```

The example represents one single-channel amplitude chip with a schematic
128-by-128 spatial grid and a 40-class score vector. It prints **shapes and data
descriptions only**. It does not supply predicted scores, a predicted class,
attention maps, evaluation metrics, a hidden model backend, or trained weights.

`example_input.json` is metadata describing a synthetic input, not a real SAR
sample or a dataset manifest. The script requires Python 3.9+ and no external
packages. It intentionally exposes no method implementation.
