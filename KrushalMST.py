# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:47:00 2019

@author: balam
"""

import tsplib95 as tsp
from heapq import heappush, heappop
import math
import numpy as np

from display import display

class graph:
    
    def __init__(self, _tspP: tsp.Problem ):
        self.tspP = _tspP
        self.heapGraph = []
        self.v = self.tspP.dimension
        self.e = len(list(self.tspP.get_edges()))
        self.parent = dict()
        self.rank = dict()
        self.result = []
        
    def initParentRank(self):
        for i in self.tspP.get_nodes():
            self.parent[i] = i
            self.rank[i] = 0
     
    def initHeapGraph(self):
        self.heapGraph = []
        for edge in self.tspP.get_edges():
            n1 , n2 = edge
            dist = self.tspP.wfunc(n1,n2)
            heappush(self.heapGraph, (dist, n1, n2))
    
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        else:
            return self.findParent(self.parent[node])
    
    def union(self, n1, n2):
        n1parent = self.findParent(n1)
        n2parent = self.findParent(n2)
        
        if self.rank[n1parent] > self.rank[n2parent]:
            self.parent[n2parent] = n1parent
        elif self.rank[n1parent] < self.rank[n2parent]:
            self.parent[n1parent] = n2parent
        else:
            self.parent[n2parent] = n1parent
            self.rank[n1parent] += 1
    
    def krushalMST(self, disp :display):
        self.result = []
        self.mstCost = math.nan
        self.initHeapGraph()
        self.initParentRank()
        
        while len(self.result) < self.v - 1:
            [w, n1, n2] = heappop(self.heapGraph)
            n1parent = self.findParent(n1)
            n2parent = self.findParent(n2)
            if n1parent != n2parent:
                self.result.append((w, n1, n2))
                self.union(n1parent,n2parent)
                disp.addEdge(self.tspP.node_coords[n1], self.tspP.node_coords[n2])
        self.mstCost = sum([i[0] for i in self.result])
        print("MST cost : ", self.mstCost)
                
    def getTour(self):
        stack = []
        tour = []
        nodes = np.asarray(list(self.parent.keys()))
        parents = np.asarray(list(self.parent.values()))
        for i in np.where((nodes == parents) == True)[0]:
            stack.append(nodes[i])
            parents[i] = -1
        while len(stack) > 0:
            node = stack.pop(-1)
            tour.append(node)
            for i in np.where((parents == node) == True)[0]:
                stack.append(nodes[i])
        return tour
            
            
        