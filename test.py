# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:34:45 2019

@author: balam
"""

import tsplib95 as tsp
import numpy as np
import math

from display import display
from MST import graph

def distance(a,b):    
    return tsp.distances.euclidean(a, b, round = float)

disp = display()

#p = tsp.utils.load_problem("Data/eil51.tsp", special = distance)
p = tsp.utils.load_problem("Data/test2.tsp", special = distance)
p.edge_weight_type = 'SPECIAL'
p.special = distance
s = tsp.utils.load_solution("Data/eil51.out.tour")

disp.addPoints(p.node_coords)
#disp.addTour(p.node_coords,s.tours[0])
#disp.addEdge(p.node_coords[1],p.node_coords[2])

print("Number of Nodes: ", len(list(p.get_nodes())))
print("Number of Edges: ", len(list(p.get_edges())))
print("Distance between nodes (1,2): ", p.wfunc(1,2))

graphMST = graph(p)
graphMST.kruskalMSTEdges(disp)
graphMST.genTree()
#disp.addTour(p.node_coords,graphMST.getTour_NoHeuristic())
#print("Tour Length No Heuristic: ", graphMST.calcTourLength())
disp.addTour(p.node_coords,graphMST.getTour_nChildHeuristic())
print("Tour Length Nearest Child First Heuristic: ", graphMST.calcTourLength())
#disp.addTour(p.node_coords,graphMST.getTour_nnHeuristic())
#print("Tour Length Nearest NN Heuristic: ", graphMST.calcTourLength())
