# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:23:56 2019

@author: balam
"""

import tsplib95 as tsp
import time

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
        
    dispMST = display(f'{filename} - MST')
    
    print(f'File Name : {filename}')
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
        t = time.time()
        d.addTour(p.node_coords,h())
        length = graphMST.calcTourLength()
        tourLengths.append(length)
        print(f'{d.title} : {length:.3f}')
        print(f'{d.title} : Time - {(time.time() - t):.3f} S')
        d.displayTourLength(length)
        
    graphMST.writeTourFile(filename)
        
# =============================================================================
#     dispMST.saveFigure("Results/Images")
#     for d in disp:
#         d.saveFigure("Results/Images")
# =============================================================================

    return tourLengths


if __name__ == '__main__':
    FindTSPTour('Data/eil101.tsp')
        
