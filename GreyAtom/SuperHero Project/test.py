# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:29:40 2020

@author: Mrityunjay1.Pandey
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({"vals": np.random.RandomState(31).randint(-30, 30, size=15), 
                   "grps": np.random.RandomState(31).choice(["A", "B"], 15)})

def replace(group):
    mask = group<0
    print(mask)
    group[mask] = group[~mask].mean()
    return group

df['patched_vals']=df.groupby(['grps'])['vals'].transform(replace)

hht
hhh
htt
hth
thh
tht
tth
ttt

