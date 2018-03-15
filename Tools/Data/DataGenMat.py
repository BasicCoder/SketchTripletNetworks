#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
import os.path as osp
import sys
import json
import scipy.io
import re

def default_image_loader(path):
    # return plt.imread(path)
    return Image.open(path).convert('RGB')

def main(base_path, filenames, prefix = "shoes", mode="train"):
    if not osp.exists(osp.join(base_path, "annotation", filenames)):
        print("Can't find annotation file!")
        sys.exit(1)
    json_filename = osp.join(base_path, "annotation", filenames)
    with open(json_filename) as f:
        info = json.load(f)
        test_image_names = info['test']['images']
        test_sketch_names = info['test']['sketches']
        test_triplets = info['test']['triplets']

        train_image_names = info['train']['images']
        train_sketch_names = info['train']['sketches']
        train_triplets = info['train']['triplets']

    test_image_paths = []
    for name in test_image_names:
        test_image_paths.append(osp.join(base_path, 'test', 'images', name))

    test_sketch_paths = []
    for name in test_sketch_names:
        test_sketch_paths.append(osp.join(base_path, 'test', 'sketches', name))

    train_image_paths = []
    for name in train_image_names:
        train_image_paths.append(osp.join(base_path, 'train', 'images', name))
    
    train_sketch_paths = []
    train_pseudo_image_paths = []
    for name in train_sketch_names:
        train_sketch_paths.append(osp.join(base_path, 'train', 'sketches', name))
        train_pseudo_image_paths.append(osp.join(base_path, 'train', 'pseudo_images', '-outputs.'.join(re.split('\.', name))))

    if mode == "train":
        images = []
        for name in train_image_paths:
            print(name)
            img_data = default_image_loader(name)
            img_data = np.asarray(img_data)
            img_data = np.expand_dims(img_data, axis=0)
            images.append(img_data)
        images = np.concatenate(images, axis=0)
        print(images.shape)
        scipy.io.savemat( prefix + '_image_db_train.mat', {'data':images})

        pseudo_images = []
        for name in train_pseudo_image_paths:
            print(name)
            pseudo_img_data = default_image_loader(name)
            pseudo_img_data = np.asarray(pseudo_img_data)
            pseudo_img_data = np.expand_dims(pseudo_img_data, axis=0)
            pseudo_images.append(pseudo_img_data)
        pseudo_images = np.concatenate(pseudo_images, axis=0)
        print(pseudo_images.shape)
        scipy.io.savemat( prefix + '_pseudo_image_db_train.mat', {'data':pseudo_images})



if __name__ == "__main__":
    record_dir = "/home/bc/Work/Database/sbir_cvpr2016/sbir_cvpr2016_release/sbir_cvpr2016/shoes"
    main(base_path = record_dir, filenames = 'shoes_annotation.json', prefix = 'shoes')
