# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:19:30 2020

@author: Mrityunjay1.Pandey
"""
path="./data_IntervalEstimate.csv"
# import packages
import pandas as pd
import numpy as np
from scipy import stats
import math

# Dataframe
data = pd.read_csv(path)

# sample size
sample_size=100

# z-critical Score
z_critical=stats.norm.ppf(q=0.95)

# sampling the dataframe
data_sample=data.sample(n=sample_size, random_state=0)

# finding the mean of the sample
sample_mean=data_sample.SalePrice.mean()

# finding the standard deviation of the population
population_std=data.SalePrice.std()

# finding the margin of error
margin_of_error=z_critical*(population_std/math.sqrt(sample_size))

