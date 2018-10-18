#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 23:12:52 2018

@author: shivam
"""

import numpy as np
#import cPickle as pickle
import pickle
import os

def load_cifar_batch(FileName):
    with open(FileName, 'rb') as f:
        data = pickle.load(f, encoding='bytes')
        X = data[b"data"]
        Y = np.array(data[b"labels"])
        return X, Y
    
#use file name for importing data