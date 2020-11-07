"""
@author: yehuawei

This file generates the testing scenario based on the parameter specified in
 "On the performance of sparse process structures in partial postponement production systems" by Chou et al (2014). 
 
 This file generates an testing case where all parameters are specified in the main function

The testing case is saved into a .pkl file where its prefix is 'input_Obermeyerm',
followed by 'mX' where X specifies the number of source nodes,
followed by 'nY' where Y specifies the number of sink nodes,
then followed by 'cvNone' which uses coefficient of variation of the demand specified 
in Chou et al (2014). 

"""


import numpy as np
import os
import pickle




if __name__ == "__main__":
    
    m=10; n=10
    
    
    #capacity vector
    mean_c = np.array([1017, 1042,  1358, 2525, 1100, 2150, 1113, 4017, 3296, 2383])
    #average demand vector
    mean_d = np.array([1017, 1042,  1358, 2525, 1100, 2150, 1113, 4017, 3296, 2383])
    #demand standard deviation vector
    sd_d = np.array([194, 323, 248, 340, 381, 404, 524, 556, 1047, 697])
    coef_var = None
    #coef_var = 0.8
    #sd_d = coef_var*mean_d
    
    #profit matrix
    profit_mat = np.ones((m,n))
    price = [110, 99, 80, 90, 123, 173, 133, 73, 93, 148]
    for i in range(m):
        for j in range(n):
            profit_mat[i,j] = price[j]*0.24
    
    #target_arc = # of arcs in the network; this is different values of target arcs to compute
    target_arcs = list(range(n,n+2*m,3))
    
    #First stage costs -- fixed cost of each arc
    fixed_costs = np.zeros((m,n))
    
    #Starting network
    flex_0 = np.zeros((m,n))
    
    with open("input_Obermeyerm{}n{}_cv{}.pkl".format(m,n,coef_var), 'wb') as f:
        pickle.dump([m,n],f) 
        pickle.dump(mean_c ,f)
        pickle.dump(mean_d,f)
        pickle.dump(sd_d,f)
        pickle.dump(profit_mat,f)
        pickle.dump(target_arcs,f)
        pickle.dump(fixed_costs,f)
        pickle.dump(flex_0,f)
    
