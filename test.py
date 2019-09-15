# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:34:45 2019

@author: balam
"""

import tsplib95 as tsp
import numpy as np
import math

from display import display
from KrushalMST import graph

def distance(a,b):    
    return tsp.distances.euclidean(a, b, round = float)

disp = display()

p = tsp.utils.load_problem("Data/test.tsp", special = distance)
p.edge_weight_type = 'SPECIAL'
p.special = distance
s = tsp.utils.load_solution("Data/eil51.out.tour")

disp.addPoints(p.node_coords)
#disp.addTour(p.node_coords,s.tours[0])
#disp.addEdge(p.node_coords[1],p.node_coords[2])

print(len(list(p.get_nodes())))
print(len(list(p.get_edges())))
print(p.wfunc(1,2))

graphMST = graph(p)
graphMST.krushalMST(disp)
disp.addTour(p.node_coords,graphMST.getTour())