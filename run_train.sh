#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=2 python Train.py \
    --batch-size 128 \
    --margin 0.3