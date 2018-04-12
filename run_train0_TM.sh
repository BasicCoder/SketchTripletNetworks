#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=0 python Train_TM.py \
    --batch-size 64 \
    --margin 0.3 \
    --resume ./runs/PretrainedModel/sketch_a_net_model_best.pth.tar