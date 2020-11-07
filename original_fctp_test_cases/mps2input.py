"""
@author: yehuawei

"""

import pickle
import re

import numpy as np
from gurobipy import *

'''
This function takes a mps file from the Fixed Charge Transportation Benchmark testing case,
and convert it into a testing case for the flexibility design problem.

The new testing case is saved into a .pkl file where its prefix is 'input',
followed by the name of the mps file, 
then followed by 'cvXXX' which specifies the coefficient of variation of the demand.


The conversion is done by setting capacity of the source nodes and the fixed costs of the arcs of the original problem;
setting the demand of the sink node as expected demand, and set the standard deviation of the demand of the sink node as 
(expected demand * coef_var);
and setting profit_mat[i,j] for arc connecting from source node i to sink/demand node j as
P - t_{ij}, where t_{ij} is the transportation cost from i to j in the original problem, 
P = max_{(i,j)} (I_{ij} + t_{ij}), and I_{ij} is the fixed charge on having arc (i,j).

Note that we choose profit_mat[i,j] so that we retain a problem equivalent to the original
fixed charge transportation problem when coef_var=0.

'''


def load_mps(mps_filename, coef_var):
    model = read(mps_filename)
    # Extract the number of supply and demand nodes from the constraints
    m = 0
    n = 0
    csts = model.getConstrs()
    for i in csts:
        if i.ConstrName[0] == 'A':
            m += 1
        elif i.ConstrName[0] == 'B':
            n += 1

    # Extract the average capacity and demand from the constraints
    mean_c = np.zeros(m)
    mean_d = np.zeros(n)
    for i in csts:
        if i.ConstrName[0] == 'A':
            aIndex = re.findall(r'\d+', i.ConstrName)
            print(aIndex)
            mean_c[int(aIndex[0])] = i.RHS

        elif i.ConstrName[0] == 'B':
            bIndex = re.findall(r'\d+', i.ConstrName)
            print(bIndex)
            mean_d[int(bIndex[0])] = i.RHS

    # demand standard deviation vector
    sd_d = mean_d * coef_var

    # Extract the profit_mat and fixed_costs from the objective coefficients of the X and Y variables
    cost_mat = np.zeros((m, n))
    fixed_costs = np.zeros((m, n))


    vrs = model.getVars()
    for var in vrs:
        print("var {}: {} {}".format(var.VarName, var.Obj, var.VType))
        vIndex = re.findall(r'\d+', var.VarName)
        i = int(vIndex[0]) // n
        j = int(vIndex[0]) % n
        if var.VarName[0] == 'X':
            cost_mat[i, j] = var.Obj
        elif var.VarName[0] == 'Y':
            fixed_costs[i, j] = var.Obj

    # the profit of a flow is set to 2 times the max flow cost on an arc - the flow cost
    costsum_mat = cost_mat + fixed_costs
    profit_mat = costsum_mat.max() - cost_mat

    flex_0 = np.zeros((m, n))

    name = mps_filename = mps_filename.split('.')[0]
    with open("input_{}_cv{}.pkl".format(name, coef_var), 'wb') as f:
        pickle.dump([m, n], f)
        pickle.dump(mean_c, f)
        pickle.dump(mean_d, f)
        pickle.dump(sd_d, f)
        pickle.dump(profit_mat, f)
        pickle.dump(fixed_costs, f)
        pickle.dump(flex_0, f)


if __name__ == "__main__":

    # Read the .mps file (math programming model) using gurobipy
    # The mps model contains a fixed charge transportation problem. The capacity
    # and demand are provided in the model constraints named under 'A' and 'B'

    # The first stage arc variables are named by 'X' and the fixed_costs corresponds to the coefficients of X variables
    # second stage flow variables are named by 'Y' and the profit_mat corresponds to -1*coefficients of Y variables
    mps_filename = "ran10x10a.mps"
    coef_var = 0.8

    dir = os.getcwd()
    files = os.listdir(dir)

    for file in files:
        if '.mps' in file:
            load_mps(file, coef_var)
