# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:23:56 2019

@author: balam
"""

import tsplib95 as tsp

from display import display
from MST import graph

def distance(a,b):    
    return tsp.distances.euclidean(a, b, round = float)

def FindTSPTour(filename):
    p = tsp.utils.load_problem(filename, special = distance)
    p.edge_weight_type = 'SPECIAL'
    p.special = distance
    
    graphMST = graph(p)
    heuristics = [graphMST.getTour_NoHeuristic,
                  graphMST.getTour_nnHeuristic,
                  graphMST.getTour_nChildHeuristic,
                  graphMST.getTour_nnAtLeaf,
                  graphMST.getTour_2opt]
    
    disp = []
    for title in ["No Heuristic",
              "Nearest Neighbour",
              "Nearest Child First",
              "Nearest Neighbour at Leaf",
              "2-OPT over NN at Leaf"]:
        disp.append(display(f'{filename} - {title}'))
        
    dispMST = display("MST")
    
    print("Number of Nodes: ", len(list(p.get_nodes())))
    print("Number of Edges: ", len(list(p.get_edges())))
    print("Distance between nodes (1,2): ", p.wfunc(1,2))
    
    
    graphMST.kruskalMSTEdges()
    graphMST.genTree()
    
    dispMST.addPoints(p.node_coords)
    dispMST.addRootNode(p.node_coords[graphMST.rootNode])
    dispMST.addEdges(p,graphMST.result)
    
    for d in disp:
        d.addPoints(p.node_coords)
        d.addRootNode(p.node_coords[graphMST.rootNode])
    
    tourLengths = []
    for h, d in zip(heuristics, disp):
        d.addTour(p.node_coords,h())
        length = graphMST.calcTourLength()
        tourLengths.append(length)
        print(f'{d.title} : {length}')
        d.displayTourLength(length)
        
    graphMST.writeTourFile(filename)
        
    return tourLengths




if __name__ == '__main__':
    FindTSPTour('Data/Random/100RandomPoints.tsp')