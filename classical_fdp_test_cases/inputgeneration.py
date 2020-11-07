#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:20:01 2020
@author: yehuawei

This file generates an testing case where all parameters are specified in the main function

The testing case is saved into a .pkl file where its prefix is 'input',
followed by 'mX' where X specifies the number of source nodes,
followed by 'nY' where Y specifies the number of sink nodes,
then followed by 'cvXXX' which specifies the coefficient of variation of the demand.

"""


import numpy as np
import pickle

if __name__ == "__main__":

    m=8; n=12
    
    
    #capacity vector
    mean_c = 100*np.ones(m) 
    #average demand vector
    mean_d = sum(mean_c)/n*np.ones(n)
    #demand standard deviation vector
    coef_var = 0.8
    sd_d = mean_d*coef_var
    
    #profit matrix
    profit_mat = np.ones((m,n))
    
    #target_arc = # of arcs in the network; this is different values of target arcs to compute
    target_arcs = list(range(n,n+3*m,3))
    
    #First stage costs -- fixed cost of each arc
    fixed_costs = np.zeros((m,n))
    
    #Starting network
    flex_0 = np.zeros((m,n))
    
    with open("input_m{}n{}_cv{}.pkl".format(m,n,coef_var), 'wb') as f:
        pickle.dump([m,n],f) 
        pickle.dump(mean_c ,f)
        pickle.dump(mean_d,f)
        pickle.dump(sd_d,f)
        pickle.dump(profit_mat,f)
        pickle.dump(target_arcs,f)
        pickle.dump(fixed_costs,f)
        pickle.dump(flex_0,f)
        
