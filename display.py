# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:46:20 2019

@author: balam
"""

import matplotlib.pyplot as plt

class display:
    
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        
    def addPoints(self,ptsDict):
        for pt in ptsDict.values():
            self.ax.scatter(pt[0],pt[1], s = 50, c='red', alpha=0.5)
        plt.show()
        
    def addTour(self,ptsDict, tour):
        x = [ptsDict[i][0] for i in tour]
        y = [ptsDict[i][1] for i in tour]
        self.ax.plot(x,y, c = 'yellow' , alpha = 0.5, lw = 5)
        plt.show()
    
    def addEdge(self, pt1,pt2):
        pts = [pt1,pt2]
        x = [i[0] for i in pts]
        y = [i[1] for i in pts]
        self.ax.plot(x,y, c = 'blue' , alpha = 1, lw = 1)
        plt.show()