"""
@author: yehuawei

This file generates the testing scenario based on the parameter specified in 
"Principles on the benefits of manufacturing process flexibility" by Jordan and Graves (1995). 

The testing case is saved into a .pkl file where its prefix is 'input_JG',
followed by 'mX' where X specifies the number of source nodes,
followed by 'nY' where Y specifies the number of sink nodes,
then followed by 'cvXXX' which specifies the coefficient of variation of the demand.

"""

import numpy as np
import os
import pickle

if __name__ == "__main__":

    m=8; n=16
    #capacity vector
    mean_c = [380,230,250,230,240,230,230,240]
    #average demand vector
    mean_d = [320,150,270,110,220,110,120,80,140,160,60,35,40,35,30,180]
    #demand standard deviation vector
    coef_var = 0.8
    sd_d = np.asarray([v*coef_var for v in mean_d], dtype=np.float)
    
    #profit matrix
    profit_mat = np.ones((m,n))
    
    #target_arc = # of arcs in the network; this is different values of target arcs to compute
    target_arcs = list(range(n,n+3*m,3))
    
    #First stage costs -- fixed cost of each arc
    fixed_costs = np.zeros((m,n))
    
    #Starting network
    flex_0 = np.zeros((m,n))
    
    with open("input_JGm{}n{}_cv{}.pkl".format(m,n,coef_var), 'wb') as f:
        pickle.dump([m,n],f) 
        pickle.dump(mean_c ,f)
        pickle.dump(mean_d,f)
        pickle.dump(sd_d,f)
        pickle.dump(profit_mat,f)
        pickle.dump(target_arcs,f)
        pickle.dump(fixed_costs,f)
        pickle.dump(flex_0,f)
        




