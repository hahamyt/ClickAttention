Discussions and analyses about Table 2 in Section 4.2:

Computation analysis.
Efficiency is an important performance indicator for interactive segmentation. 
To this end, we compared the differences in running speed and parameter size between ClickAttention and current SOTA algorithms, as shown in Table 2.

The model parameters of the current SOTA algorithm SimpleClick are 84.89e16 and 322.18e16, which are 1.82 times and 6.94 times larger than our largest model, respectively.
Due to its larger input size, it takes more than 10 times longer for the algorithm in question to run compared to our algorithm. 
Additionally, both RITM and FirstClick-resnet101 have a larger number of parameters than the algorithm proposed in this paper, with FirstClick-resnet101 taking 8.6 times longer to run than our algorithm. Except for FocalClick, all models have a runtime exceeding 1 second.
Due to the larger input size of SimpleClick, its inference time is more than ten times that of our algorithm. In addition, the parameter sizes of RITM and FirstClick-resnet101 are also larger than the proposed algorithm, with the inference time of FirstClick-resnet101 being 8.6 times as long as ours. Except for FocalClick, all compared models have more than 1 second running speed. Interactive segmentation algorithms are widely used in crowdsourcing annotation tasks, where device performance is typically low. Therefore, a large number of parameters can create a significant burden on devices with only a CPU, leading to reduced work efficiency.

In contrast, the Segformer-based FocalClick and ClickAttention demonstrate faster inference time.  Compared to FocalClick, ClickAttention achieved better performance at the cost of a limited loss in speed.

Discussions and analyses about About Table 1 in Section 4.2:

Performance on existing benchmarks
Classical methods such as Graph Cut  and Geodesic star convexity were not compared in the study due to their performance disadvantage.
The performance comparison results of ClickAttention and current SOTA on mainstream benchmarks are shown in Table 1.

As illustrated in Table 1, Ours-B0-S2 achieved better performance on multiple datasets compared to FocalClick-B3-S2, which also uses Segformer. In detail, Ours-B0-S2 performed 1.2% and 2.7% better than FocalClick-B3-S2 on GrabCut and DAVIS, respectively. This indicates that the proposed algorithm still has competitive performance with fewer parameters. We believe the reason for this is that the proposed algorithm fully utilizes all user clicks, whereas FocalClick's target crop operation discards points outside the target region, causing it to only refine the local regions of large targets, but ignore the overall accuracy.
In addition, compared to FocalClick-B3-S2, Ours-B3-S2 showed better performance in almost all benchmarks. As shown in Table 1, the algorithms compared performed more poorly on the SBD and DAVIS datasets. This is likely due to the fact that SBD contains over 6000 test samples, and DAVIS includes a significant number of challenging cases, resulting in relatively high values of NoC90. Ours-B3-S2 achieved the best performance on DAVIS, with a 1% improvement over the second-place algorithm SimpleClick. On SBD, our algorithm's NoC90 improved by 4.9% compared to the third-place algorithm. Combined with Table 2, the results show that our algorithm achieves competitive performance with fewer parameters. On GrabCut, Ours-B3-S2 and SimpleClick achieved the best NoC90 performance. Except for ranking fourth on the Berkeley benchmark, Ours-B3-S2's performance on other datasets is only second to SimpleClick. 
After analyzed the characteristics of the Berkeley dataset, we found that it has a low resolution (480x320) and there are many cases of intricate edges, including antlers and feathers. The performance of the proposed algorithm still needs to be improved under these conditions.

Discussions and analyses about About Table 3 in Section 4.3:

It can be found that, compared to RITM, SimpleClick, and FocalClick, ClickAttention has the best performance on the DAVIS585-SP task.  Compared with the second-ranked SimpleClick, we have improved by 5.8% on NoC90, which proves the advanced nature of the algorithm in this paper on the mask correction task. Compared to FocalClick, ClickAttention improves NoC 85 and NoC 90 in mask correction by 13% and 12.3% respectively. Compared with the second-ranked SimpleClick, we have improved by 5.8% NoC90 performance, which demonstrates the effectiveness of the proposed algorithm in mask correction tasks.

We believe the reason is that the input of the mask can provide certain prior information for the network. However, the existing algorithm only treats the mask as an additional modal feature and does not make full use of it. In our work, we mainly calculate the similarity between the user click area and other area features. Among these features, the prior mask provides consistent feature expression for the target area tokens. So that it helps the algorithm to better find all similar tokens. Compared to other methods, the algorithm proposed in this paper can make better use of prior mask information.

On the DAVIS585-ZERO task, ClickAttention ranks second, only behind SimpleClick-ViT-L, whose parameter size is 6.94 times larger than ours. Compared to FocalClick, the proposed algorithm improves NoC 85 and NoC 90 by 6.9% and 5.7% respectively. This trend is consistent with the results shown in Table 1.
