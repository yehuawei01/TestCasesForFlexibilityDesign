#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:39:17 2020

@author: yehuawei
"""
import os
import pickle
import numpy as np

if __name__ == "__main__":
    
    experiment = "JGm8n16_cv0.8"
    #experiment = "ran10x10a_cv0.8"

    input_file_name = os.getcwd() + "/input_" + experiment + ".pkl"
    with open(input_file_name, 'rb') as f:
        m, n = pickle.load(f)
        mean_c = pickle.load(f)
        mean_d = pickle.load(f)
        sd_d = pickle.load(f)
        profit_mat = pickle.load(f)
        fixed_costs = pickle.load(f)
        flex_0 = pickle.load(f)

    #generating 100 samples of demand vectors based on the mean_d and sd_d
    num_samples = 100
    demand_samples = np.zeros((n, num_samples))

    for i in range(num_samples):
        demand = np.random.normal(mean_d, sd_d)
        # truncate demand at two standard deviations and ensure that it is positive
        demand = np.maximum(demand, 0)
        demand = np.maximum(demand, mean_d - 2 * sd_d)
        demand = np.minimum(demand, mean_d + 2 * sd_d)
        demand_samples[:, i] = demand
