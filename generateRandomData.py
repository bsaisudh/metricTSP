# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:33:16 2019

@author: balam
"""

import matplotlib.pyplot as plt
import numpy as np

def generateX(n,m):
    Xmu = [50]*n
    Xcov = np.diag([100]*n)
    X = np.random.multivariate_normal(Xmu, Xcov, m)
    print ("shape of X : ", X.shape)
    plt.plot(X[:,0], X[:,1], 'or')
    plt.show()
    return X


def generateX_u(n,m):
    X = []
    for i in range(n):
        X.append(np.random.uniform(low=10, high=100, size=m))
    X = np.asarray(X)
    X = X.T
    print ("shape of X : ", X.shape)
    plt.plot(X[:,0], X[:,1], 'or')
    plt.show()
    return X

def TSPfileWrite(filename,n,m):
    header = f'''NAME : {filename}
COMMENT : {100} Random points test
TYPE : TSP
DIMENSION : {m}
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
'''
    with open(f'Data/Random/{filename}.tsp','w+') as f:
        f.write(header)
        for i,pt in enumerate(generateX_u(n,m)):
            f.write(f'{i+1} {pt[0]:.2f} {pt[1]:.2f}\n')
        f.write(f'EOF')



if __name__ == '__main__':
    n = 2
    m = 100
    filename = f'{m}RandomPoints'
    TSPfileWrite(filename,n,m)

