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

disp0 = display("MST")
disp1 = display("NN Neighbour")
disp2 = display("2 Opt")

p = tsp.utils.load_problem("Data/eil101.tsp", special = distance)
#p = tsp.utils.load_problem("Data/test.tsp", special = distance)
p.edge_weight_type = 'SPECIAL'
p.special = distance
s = tsp.utils.load_solution("Data/eil51.out.tour")

disp0.addPoints(p.node_coords)
disp1.addPoints(p.node_coords)
disp2.addPoints(p.node_coords)

print("Number of Nodes: ", len(list(p.get_nodes())))
print("Number of Edges: ", len(list(p.get_edges())))
print("Distance between nodes (1,2): ", p.wfunc(1,2))

graphMST = graph(p)
graphMST.kruskalMSTEdges()
graphMST.genTree()

disp0.addRootNode(p.node_coords[graphMST.rootNode])
disp1.addRootNode(p.node_coords[graphMST.rootNode])
disp2.addRootNode(p.node_coords[graphMST.rootNode])

disp0.addEdges(p, graphMST.result)

#disp1.addTour(p.node_coords,graphMST.getTour_NoHeuristic())
#print("Tour Length No Heuristic: ", graphMST.calcTourLength())

#disp1.addTour(p.node_coords,graphMST.getTour_nChildHeuristic())
#print("Tour Length Nearest Child First Heuristic: ", graphMST.calcTourLength())

#disp1.addTour(p.node_coords,graphMST.getTour_nnHeuristic())
#print("Tour Length Nearest NN Heuristic: ", graphMST.calcTourLength())

#disp1.addTour(p.node_coords,graphMST.getTour_nnAtLeaf())
#print("Tour Length Nearest NN at leaf : ", graphMST.calcTourLength())

#disp2.addTour(p.node_coords,graphMST.getTour_2opt())
#print("Tour Length 2 OPT : ", graphMST.calcTourLength())