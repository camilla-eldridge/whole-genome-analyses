#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:13:42 2021

@author: ce9
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

import cooler
import cooltools
#cool_file = cooltools.download_data("HFF_MicroC", cache=True, data_dir='./')
#print(cool_file)
#cooler.fileops.list_coolers('./test.mcool')

cooler.fileops.list_coolers('./iyVesGerm1_1.mcool')
clr = cooler.Cooler('./iyVesGerm1_1.mcool::resolutions/512000')
print(f'chromosomes: {clr.chromnames}, binsize: {clr.binsize}')
 
chromstarts = []
for i in clr.chromnames:
    print(f'{i} : {clr.extent(i)}')
    print(f'{i} :{clr.pixels}')
    chromstarts.append(clr.extent(i)[0])

f, ax = plt.subplots(
    figsize=(7,6))
im = ax.matshow((clr.matrix(balance=False)[:]),vmax=600, vmin=0);
plt.colorbar(im ,fraction=0.04, pad=0.04, label='raw counts')
ax.set(xticks=chromstarts, xticklabels=clr.chromnames,
       xlabel='position, chrom#', ylabel='position, bin#')
ax.xaxis.set_label_position('top')











