# Sketch Triplet Networks.
   A PyTorch Implementation for Sketch Triplet Networks.
   
## Model Configuration
- Optimizer
   - Adam

## Model Parameters
| Model branch | pretrained | lr | clip_grad_norm(max_norm)| learning rate decay | weight_decay |
| --- | --- | --- | --- | --- | --- |
| AlexNet | T | 2e-4 | -- | 8 | 0.0005 | 

## Model Result
| Model branch | pretrained |  Loss Function | Rank@1 | Rank@5 | Rank@10 | 
| --- | --- | --- | --- | --- | --- |
| AlexNet | T | TripletMarginLoss | 
| AlexNet | 