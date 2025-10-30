# Keras-compatible arrows8 dataset

This dataset contains binary (0 or 1) 8x8 pixel images of arrows, saved in `.npz` format. The dataset contains four classes of arrows: `up`, `left`, `down` and `right`. The dataset is formed from augmenting (5 degree rotation and random horizontal and vertical pixel shifts) synthetic, manually generated images with differing arrow designs, sizes and locations. The dataset also contains 391 images at indices above 4000 (inclusive), in all splits, that were grabbed, scaled and binarized by a web camera pointed at screen displaying images of arrows.

Dataset is suitable for use with very small, binary networks such as in the evaluation of novel neuromorphic hardware. High classification rates (>95%) are possible with two-layer feedforward networks and small numbers of hidden layer neurons.

The following samples are known to be empty (blank images):
| Split | Index |
|------ | ----- |
| Train | 4170 |
| Validation | 4023 |
| Test | 4028, 4065 |


## Contents

- `arrows8_keras_format.npz`: Compressed NumPy archive with:
  - `x_train`: shape (4274, 8, 8, 1)
  - `y_train`: shape (4274,)
  - `x_val`: shape (4039, 8, 8, 1)
  - `y_val`: shape (4039,)
  - `x_test`: shape (4078, 8, 8, 1)
  - `y_test`: shape (4078,)
  - `class_names`: shape (4,)

## How to Load

```python
import numpy as np

data = np.load('arrows8_keras_format.npz')
x_train = data['x_train']
y_train = data['y_train']
```