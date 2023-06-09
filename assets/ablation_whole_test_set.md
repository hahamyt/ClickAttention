## Ablation experiment on the whole test set


|           Method           | GrabCut | Berkeley |  SBD   |        | DAVIS  | COCO\_MVal |        | PascalVOC |        |
|:--------------------------:|:-------:|:--------:|:------:|:------:|:------:|:----------:|:------:|:---------:|:------:|
|                            | NoC 90  |  NoC 90  | NoC 85 | NoC 90 | NoC 90 |   NoC 85   | NoC 90 |  NoC 85   | NoC 90 |
|       f-BRS-B-hrnet32      |  1.69   |   2.44   |  4.37  |  7.26  |  6.50  |     -      |   -    |     -     |   -    |
|        RITM-hrnet18s       |  1.68   |   2.60   |  4.25  |  6.84  |  5.98  |     -      |  3.58  |   2.57    |   -    |
|        RITM-hrnet32        |  1.56   |   2.10   |  3.59  |  5.71  |  5.34  |    2.18    |  3.03  |   2.21    |  2.59  |
|      EdgeFlow-hrnet18      |  1.72   |   2.40   |   -    |   -    |  5.77  |     -      |   -    |     -     |   -    |
|      SimpleClick-ViT-B     |  1.50   |   1.86   |  3.38  |  5.50  |  5.18  |    2.18    |  2.92  |   2.06    |  2.38  |
|      SimpleClick-ViT-L     |  1.46   |   1.83   |  2.92  |  4.85  |  4.77  |    1.96    |  2.63  |   1.71    |  1.93  |
| FocalClick-segformer-B0-S2 |  1.90   |   2.92   |  5.14  |  7.80  |  6.47  |    3.23    |  4.37  |   3.55    |  4.24  |
| FocalClick-segformer-B3-S2 |  1.68   |   1.71   |  3.73  |  5.92  |  5.59  |    2.45    |  3.33  |   2.53    |  2.97  |
|     Ours-B0-S2-baseline    |  2.42   |   4.29   |  6.55  |  9.39  |  10.2  |    4.25    |  5.73  |   4.41    |  5.31  |
|        Ours-B0-S2+CA       |  1.60   |   2.73   |  4.77  |  7.32  |  5.65  |    2.74    |  4.01  |   3.01    |  3.52  |
|      Ours-B0-S2+CA+DAA     |  1.66   |   2.65   |  4.45  |  6.90  |  5.44  |    2.81    |  3.77  |   2.87    |  3.36  |
|    Ours-B3-S2-baseline    |  1.48  |   2.10    |   4.54 |   6.14  |   6.02  |     3.06    |  4.50   |    3.29    |   4.10    |
|    Ours-B3-S2+CA    |  1.38  |    1.93   |  3.38  |  5.42   |  4.93   |    2.13     |   2.99  |    1.99    |   2.41    |
|    Ours-B3-S2+CA+DAA    |  1.46   |   1.95   |  3.26  |  5.23  |  4.72  |    2.17    |  2.89  |   2.05    |  2.37  |

> Due to time limitations, some weights were re-trained in a short time, and as a result, some results may have subtle differences in the manuscript. But the trend is the same.
