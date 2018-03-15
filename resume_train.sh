#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=2 python Train.py \
    --batch-size 64 \
    --margin 0.3 \
    --resume ./runs/TripletNetModel/checkpoint.pth.tar