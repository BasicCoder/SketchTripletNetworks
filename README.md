# Sketch Triplet Networks.
   A PyTorch Implementation for Sketch Triplet Networks.
   
## Model Configuration
- Optimizer
   - Adam

## DataSet


## Model Parameters
| Model branch | pretrained   | Loss Function     | lr   | clip_grad_norm(max_norm) | learning rate decay | weight_decay | Margin |
| ------------ | ------------ | ----------------- | ---- | ------------------------ | ------------------- | ------------ | ------ |
| AlexNet      | T(ImageNet)  |                   | 2e-4 | 1.0                      | 100                 | 0.0003       | 0.3    |
| ResNet18     | T            | MarginRankingLoss | 2e-6 | 10.0                     | 20                  | 0.05         | 0.3    |
| ResNet18     | T(TU-Berlin) | TripletMarginLoss | 2e-6 | 10.0                     | 20                  | 0.01         | 0.3    |

## Model Result
### Shoes
#### Train Set(ranking)
| Model branch | pretrained   | Loss Function     | prec | mprec |
| ------------ | ------------ | ----------------- | ---- | ----- |
| AlexNet      | T            | TripletMarginLoss |      |       |
| ResNet18     | T            | MarginRankingLoss |      |       |
| ResNet18     | T(ImageNet)  | TripletMarginLoss |      |       |
| ResNet18     | T(TU-Berlin) | TripletMarginLoss |      |       |

#### Test Set(ranking)
| Model branch | pretrained   | Loss Function     | prec  | mprec |
| ------------ | ------------ | ----------------- | ----- | ----- |
| AlexNet      | T            | TripletMarginLoss | 61.76 | 15.34 |
| ResNet18     | T            | MarginRankingLoss |       |       |
| ResNet18     | T(ImageNet)  | TripletMarginLoss |       |       |
| ResNet18     | T(TU-Berlin) | TripletMarginLoss |       |       |

#### Test Set(retrieval)
| Model branch | pretrained         | Loss Function                     | Rank@1 | Rank@5 | Rank@10 | corr  |
| ------------ | ------------------ | --------------------------------- | ------ | ------ | ------- | ----- |
| Origin       |                    | Triplet Loss                      | 39.13  | --     | 87.83   | 69.49 |
| AlexNet      | T                  | TripletMarginLoss                 |        |        |         |       |
| ResNet18     | TU-Berlin          | TripletLoss                       | 26.957 | 51.304 | 64.348  | 64.54 |  |
| ResNet18     | T                  | MarginRankingLoss                 |        |        |         |       |
| ResNet18     | TU-Berlin          | MarginRankingLoss                 | 29.565 | 50.435 | 69.565  | 64.21 |
| ResNet18     | ImageNet           | TripletMarginLoss                 |        |        |         |       |
| ResNet18     | TU-Berlin          | TripletMarginLoss                 | 25.217 | 53.043 | 65.217  | 64.79 |
| ResNet18     | TU-Berlin          | TripletMarginLoss + embedded_norm |        |        |         |       |
| SketchANet   | ImageNet TU-Berlin | Triplet Loss(square_distance)     | 52.174 |        | 92.174  |       |
