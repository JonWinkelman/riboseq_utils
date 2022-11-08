#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:11:25 2022

@author: jonwinkelman
"""
import pandas as pd

path_to_valcounts_dir = './data/value_counts'
list_of_valcount_paths = get_filepaths_in_dir(path_to_valcounts_dir, end_to_exclude='.DS_Store')
path = list_of_valcount_paths[0]
def filt_peak_singletons(path, mult = 20):
    df = pd.read_csv(path)
    df.columns = ['genomic_position', df.columns[1],df.columns[2]] 
    df = df.set_index('genomic_position')
    d_lst = [df.iloc[:,0].to_dict(), df.iloc[:,1].to_dict()]
    suspect_positions = {}
    for d in d_lst:
        for pos in d.keys():
            hits = d[pos]
            prev = d.get(pos-1)
            post = d.get(pos+1)
            if not prev: prev=1
            if not post: post=1
            if hits>mult*prev and hits>mult*post:
                suspect_positions[pos]=d[pos]
    return suspect_positions

            

        
    
    
