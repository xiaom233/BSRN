# BSRN[Paper Link](https://arxiv.org/abs/2205.05996)  
Blueprint Separable Residual Network for Efficient Image Super-Resolution  
Zheyuan Li, Yingqi Liu, Xiangyu Chen, Haoming Cai, Jinjin Gu, Yu Qiao, Chao Dong

BibTex
```
@InProceedings{Li_2022_CVPR,
    author    = {Li, Zheyuan and Liu, Yingqi and Chen, Xiangyu and Cai, Haoming and Gu, Jinjin and Qiao, Yu and Dong, Chao},
    title     = {Blueprint Separable Residual Network for Efficient Image Super-Resolution},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2022},
    pages     = {833-843}
}
```

## Environment

[PyTorch >= 1.7](https://pytorch.org/)
[BasicSR >= 1.3.4.9](https://github.com/XPixelGroup/BasicSR)

### Installation
```
pip install -r requirements.txt
python setup.py develop
```

## How To Test
· Refer to ./options/test for the configuration file of the model to be tested, and prepare the testing data and pretrained model.  
· The pretrained models are available in ./experiments/pretrained_models/  
· Then run the follwing codes (taking net_g_BSRN_x4.pth as an example):  

```
python basicsr/test.py -opt options/test/benchmark_BSRN_x4.yml
```
The testing results will be saved in the ./results folder.

## How To Train
· Refer to ./options/train for the configuration file of the model to train.  
· Preparation of training data can refer to this page. All datasets can be downloaded at the official website.  
· The training command is like  
```
CUDA_VISIBLE_DEVICES=0 python bascisr/train.py -opt options/train/train_BSRN_x4.yml
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.launch --nproc_per_node=4 --master_port=4321 basicsr/train.py -opt options/train/train_BSRN-S_x4.yml --launcher pytorch
```
For more training commands and details, please check the docs in [BasciSR](https://github.com/XPixelGroup/BasicSR)  

## Results
The inference results on benchmark datasets are available at [Google Drive](https://drive.google.com/drive/folders/18uRxyAWwpAfKuxgDneacJkF4-rAyR7XR?usp=sharing) or [Baidu Netdisk](https://pan.baidu.com/s/1N9zLwsOBM8MxqpfK5zpZXw) (access code: VISU).

## Contact
If you have any question, please email zy.li3@siat.ac.cn or join in the Wechat group of BasicSR to discuss with the authors.