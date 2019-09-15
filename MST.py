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
    
    def findGrandParent(self, node):
        if self.parent[node] == node:
            return node
        else:
            return self.findGrandParent(self.parent[node])
    
    def union(self, n1, n2):
        n1Gparent = self.findGrandParent(n1)
        n2Gparent = self.findGrandParent(n2)
        
        if self.rank[n1Gparent] > self.rank[n2Gparent]:
            self.parent[n2Gparent] = n1Gparent
        elif self.rank[n1Gparent] < self.rank[n2Gparent]:
            self.parent[n1Gparent] = n2Gparent
        else:
            self.parent[n2Gparent] = n1Gparent
            self.rank[n1Gparent] += 1
    
    def kruskalMSTEdges(self, disp :display):
        self.result = []
        self.mstCost = math.nan
        self.initHeapGraph()
        self.initParentRank()
        
        while len(self.result) < self.v - 1:
            [w, n1, n2] = heappop(self.heapGraph)
            n1Gparent = self.findGrandParent(n1)
            n2Gparent = self.findGrandParent(n2)
            if n1Gparent != n2Gparent:
                self.result.append((w, n1, n2))
                self.union(n1Gparent,n2Gparent)
                disp.addEdge(self.tspP.node_coords[n1], self.tspP.node_coords[n2])
        self.mstCost = sum([i[0] for i in self.result])
        print("MST cost : ", self.mstCost)
        
    def genTree(self):
        stack = []
        self.tree = dict()
        edges = np.asarray([[n1,n2] for w,n1,n2 in self.result])
        nodes = np.asarray(list(self.parent.keys()))
        parents = np.asarray(list(self.parent.values()))
        for i in np.where((nodes == parents) == True)[0]:
            stack.append(nodes[i])
            self.tree[nodes[i]] = nodes[i]
        while len(stack) > 0:
            node = stack.pop(-1)
            childEdges = np.where(edges == node)
            if childEdges[0].size > 0 :
                for childEdge in zip(childEdges[0],childEdges[1]):
                    stack.append( edges [ childEdge[0] ] [ int(not(childEdge[1])) ] )
                    self.tree[ edges [ childEdge[0] ] [ int(not(childEdge[1])) ] ] = node
                    edges[childEdge[0],:] = [-1, -1]
                
    def getTour_NoHeuristic(self):
        stack = []
        self.tour = []
        nodes = np.asarray(list(self.tree.keys()))
        parents = np.asarray(list(self.tree.values()))
        for i in np.where((nodes == parents) == True)[0]:
            stack.append(nodes[i])
            parents[i] = -1
        while len(stack) > 0:
            node = stack.pop(-1)
            self.tour.append(node)
            for i in np.where((parents == node) == True)[0]:
                stack.append(nodes[i])
        return self.tour
    
    def getTour_nChildHeuristic(self):
        stack = []
        self.tour = []
        nodes = np.asarray(list(self.tree.keys()))
        parents = np.asarray(list(self.tree.values()))
        for i in np.where((nodes == parents) == True)[0]:
            stack.append(nodes[i])
            parents[i] = -1
        while len(stack) > 0:
            node = stack.pop(-1)
            self.tour.append(node)
            childs = []
            for i in np.where((parents == node) == True)[0]:
                dist = self.tspP.wfunc(node, nodes[i])
                childs.append([dist, nodes[i]])
            for dist, child in sorted(childs, reverse = True):
                stack.append(child)
        return self.tour
    
    def getTour_nnHeuristic(self):
        stack = []
        self.tour = []
        nodes = np.asarray(list(self.tree.keys()))
        parents = np.asarray(list(self.tree.values()))
        for i in np.where((nodes == parents) == True)[0]:
            stack.append(nodes[i])
            parents[i] = -1
        while len(stack) > 0:
            if len(self.tour) > 0:
                cNode = self.tour[-1]
                stackParents = []
                for i in stack:
                    if self.tree[i] == i:
                        stackParents.append(-1)
                    else:
                        stackParents.append(self.tree[i])
                if np.where(stackParents == self.tree[cNode])[0].size > 0 :
                    nextNodes = []
                    for i in np.where(stackParents == self.tree[cNode])[0]:
                        nextNodes.append(stack[i])
                    nodeDistances = [[self.tspP.wfunc(i,cNode), i] for i in nextNodes]
                    nodeDistances = sorted(nodeDistances)
                    minDistNode = nodeDistances[0][1]
                    node = stack.pop(np.where(stack == minDistNode)[0][0])
                else:
                    node = stack.pop(-1)
            else:
                node = stack.pop(-1)
                
            self.tour.append(node)
            childs = []
            for i in np.where((parents == node) == True)[0]:
                dist = self.tspP.wfunc(node, nodes[i])
                childs.append([dist, nodes[i]])
            for dist, child in sorted(childs, reverse = True):
                stack.append(child)
        return self.tour
    
    def calcTourLength(self):
        tourLength = 0
        for i in range(len(self.tour)-1):
            tourLength += self.tspP.wfunc(self.tour[i],self.tour[i+1])
        return tourLength
            
        