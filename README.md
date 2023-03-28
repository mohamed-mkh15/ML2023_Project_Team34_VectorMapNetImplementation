# ML2023_Project_Team34_VectorMapNetImplementation
This repo includes the code, report, and presentation for the final project of the machine learning course at Skoltech. It also includes a colab for the Map_merge algorithm that's still under developing. 

The results are shown for the main code using their checkpoint and our implementation for it. 


# VectorMapNet_code
**VectorMapNet: End-to-end Vectorized HD Map Learning**

This is a fork of the official codebase of VectorMapNet


[Yicheng Liu](https://scholar.google.com/citations?user=vRmsgQUAAAAJ&hl=zh-CN), Yuantian Yuan, [Yue Wang](https://people.csail.mit.edu/yuewang/), [Yilun Wang](https://scholar.google.com.hk/citations?user=nUyTDosAAAAJ&hl=en/), [Hang Zhao](http://people.csail.mit.edu/hangzhao/)


**[[Paper](https://arxiv.org/pdf/2206.08920.pdf)] [[Project Page](https://tsinghua-mars-lab.github.io/vectormapnet/)]**

**Abstract:**
Autonomous driving systems require a good understanding of surrounding environments, including moving obstacles and static High-Definition (HD) semantic maps. Existing methods approach the semantic map problem by offline manual annotations, which suffer from serious scalability issues. More recent learning-based methods produce dense rasterized segmentation predictions which do not include instance information of individual map elements and require heuristic post-processing that involves many hand-designed components, to obtain vectorized maps. To that end, we introduce an end-to-end vectorized HD map learning pipeline, termed VectorMapNet. VectorMapNet takes onboard sensor observations and predicts a sparse set of polylines primitives in the bird's-eye view to model the geometry of HD maps. Based on this pipeline, our method can explicitly model the spatial relation between map elements and generate vectorized maps that are friendly for downstream autonomous driving tasks without the need for post-processing. In our experiments, VectorMapNet achieves strong HD map learning performance on nuScenes dataset, surpassing previous state-of-the-art methods by 14.2 mAP. Qualitatively, we also show that VectorMapNet is capable of generating comprehensive maps and capturing more fine-grained details of road geometry. To the best of our knowledge, VectorMapNet is the first work designed toward end-to-end vectorized HD map learning problems.


# Run VectorMapNet

## 0. Environment

Set up environment by following this [script](Fork_VectorMapNet_code/env.md)

## 1. Prepare your dataset

Store your data with following structure (inside Fork_VectorMapNet_code folder):

```
    root
        |--datasets
            |--nuScenes
            |--Argoverse2(optional)

```

### 1.1 Generate annotation files

#### Preprocess nuScenes

```
python Fork_VectorMapNet_code/tools/data_converter/nuscenes_converter.py --data-root your/dataset/nuScenes/
```

## 2. Evaluate VectorMapNet

### Download Checkpoint
| Method       | Modality    | Config | Checkpoint |
|--------------|-------------|--------|------------|
| VectorMapNet | Camera only | [config](Fork_VectorMapNet_code/configs/vectormapnet.py) | [model link](https://drive.google.com/file/d/1ccrlZ2HrFfpBB27kC9DkwCYWlTUpgmin/view?usp=sharing)      |


### Train VectorMapNet

In single GPU
```
python Fork_VectorMapNet_code/tools/train.py configs/vectormapnet.py
```

For multi GPUs
```
bash Fork_VectorMapNet_code/tools/dist_train.sh configs/vectormapnet.py $num_gpu
```


### Do Evaluation

In single GPU
```
python Fork_VectorMapNet_code/tools/test.py configs/vectormapnet.py /path/to/ckpt --eval name
```

For multi GPUs
```
bash Fork_VectorMapNet_code/tools/dist_test.sh configs/vectormapnet.py /path/to/ckpt $num_gpu --eval name
```


### Expected Results 
#### Paper (after 130 epochs)

| $AP_{ped}$   | $AP_{divider}$ | $AP_{boundary}$ | mAP   |
|--------------|----------------|-----------------|-------|
| 0.956 | 0.890    | 0.699          | 0.848 |

#### Our implementation  (after 36 epochs)
| $AP_{ped}$   | $AP_{divider}$ | $AP_{boundary}$ | mAP   |
|--------------|----------------|-----------------|-------|
| 0.679 | 0.458    | 0.226          | 0.454 |
