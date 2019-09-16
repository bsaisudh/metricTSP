# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:46:20 2019

@author: balam
"""

import matplotlib.pyplot as plt

class display:
    
    def __init__(self, title):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title(title)
        
    def addPoints(self,ptsDict):
        for v, pt in zip(ptsDict.keys(), ptsDict.values()):
            self.ax.scatter(pt[0],pt[1], s = 50, c='blue', alpha=1)
            self.ax.annotate(str(v),(pt[0],pt[1]))
        plt.show()
        
    def addTour(self,ptsDict, tour):
        closedTour = []
        closedTour.extend(tour)
        closedTour.append(tour[0])
        x = [ptsDict[i][0] for i in closedTour]
        y = [ptsDict[i][1] for i in closedTour]
        self.ax.plot(x,y, c = 'green' , alpha = 0.5, lw = 5)
        plt.show()
    
    def addEdge(self, pt1,pt2):
        pts = [pt1,pt2]
        x = [i[0] for i in pts]
        y = [i[1] for i in pts]
        self.ax.plot(x,y, c = 'blue' , alpha = 1, lw = 1.5)
        plt.show()

    def addEdges(self,tspP, treeEdges):
        for w,n1,n2 in treeEdges:
            self.addEdge(tspP.node_coords[n1], tspP.node_coords[n2])
            
    def addRootNode(self, pt):
        self.ax.scatter(pt[0],pt[1], s = 80, c='red', alpha=1)
        plt.show()