# Point-of-interest-detection-and-matching
Point of interest detection and matching with sift, harris.
### Finished work

1. Use Harris corner detection algorithm to detect key points of two images with the same shooting scene but different perspectives.
2. Extract the SIFT descriptor for the key points in step 1. In order to reduce work, SIFT encoding does not implement all the steps of the algorithm, but only implements the specified content to complete a "simplified SIFT".
3. Use the key point descriptor in step 2 to perform key point matching to further estimate the transformation relationship between the two images

### Language and Environment

Python 3

The compatibility of the Python program on Windows & Linux is very good, the program does not need additional adaptation.

### result

|        | feature num | Threshold |  alpha   |  time   | Harris corners |     Harris acc     | match acc |
| :----: | :---------: | :-------: | :------: | :-----: | :------------: | :----------------: | :-------: |
|   1    |    2500     |   3000    |   0.04   |   ——    |  16979/18982   |  0.77/0.64/0.705   |   0.66    |
|   2    |    2500     |   8000    |   0.04   |   ——    |   9014/10395   |  0.79/0.80/0.795   |   0.58    |
|   3    |    4000     |   9000    |   0.04   |   927   |   8315/9615    |   1.00/0.92/0.96   |   0.70    |
|   4    |    2500     |   5000    |   0.04   |   899   |  12245/14013   |   0.74/0.37/0.55   |   0.65    |
|   5    |    2500     |   6500    |   0.04   |   881   |  10307/11886   |   0.62/1.00/0.81   |   0.62    |
|   6    |    3000     |   10000   |   0.04   |   630   |   7734/8942    |   0.33/1.00/0.66   |   0.79    |
|   7    |    3500     |   11000   |   0.04   |   652   |   7212/8395    |   1.00/0.86/0.92   |   0.75    |
|   8    |    3000     |   11000   |   0.04   |   556   |   7212/8395    |   0.59/0.62/0.60   |   0.78    |
|   9    |    3000     |   13000   |   0.04   |   524   |   6380/7504    |   0.71/0.30/0.50   |   0.74    |
|   10   |    3000     |   15000   |   0.04   |   571   |   5769/6762    |   0.51/1.00/0.75   |   0.68    |
|   11   |    3000     |   17000   |   0.04   |   487   |   5259/6155    |   0.82/1.00/0.90   |   0.60    |
|   12   |    3000     |   18000   |   0.04   |   467   |   5051/5871    |   0.63/0.65/0.64   |   0.63    |
|   13   |    3000     |   18000   |   0.08   |   72    |   2346/2865    |  0.78/0.67/0.725   |   0.15    |
|   14   |    3000     |   10000   |   0.08   |   380   |   3659/4577    |   0.76/0.62/0.69   |   0.79    |
|   15   |    3000     |   10000   |   0.06   |   441   |   5264/6397    |   0.92/0.48/0.7    |   0.74    |
|   16   |    3000     |   13000   |   0.06   |   412   |   4394/5312    |   0.39/0.99/0.69   |   0.80    |
|   17   |    3500     |   13000   |   0.06   |   509   |   4394/5312    |  1.00/0.05/0.525   |   0.80    |
|   18   |    2500     |   13000   |   0.06   |   332   |   4394/5312    |   1.00/0.38/0.69   |   0.73    |
|   19   |    3300     |   13000   |   0.06   |   477   |   4394/5312    |   0.61/0.00/0.30   |   0.80    |
| **20** |  **3300**   | **12000** | **0.06** | **477** | **4642/5625**  | **1.00/0.69/0.84** | **0.81**  |

```
ANMS cost: 51.03812289237976
before ANMS imghas corners num:4642
after ANMS imghas corners num:3300
get_interest_points cost: 68.967276096344
ANMS cost: 68.86741805076599
before ANMS imghas corners num:5625
after ANMS imghas corners num:3300
get_interest_points cost: 87.22036457061768
3300 corners in image 1, 3300 corners in image 2
get_features cost: 28.669880151748657
get_features cost: 28.00908327102661
match_features cost: 269.0517473220825
176 matches from 3300 corners
totally cost: 483.8261709213257
You found 100/100 required keypoints
one image accuracy = 1.000000
You found 100/100 required keypoints
one image accuracy = 0.690000
------------key point mean acc on  two images: 0.845 ----------
You found 100/100 required matches
--------Match Accuracy = 0.810000------
```

