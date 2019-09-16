# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:35:36 2019

@author: balam
"""

from generateRandomData import TSPfileWrite
from TSPFindTour import FindTSPTour




for i in range (10):
    n = 2
    m = 200
    filename = f'{m}RandomPoints - {i}'
    TSPfileWrite(filename,n,m)
    FindTSPTour(f"Data/Random/{filename}.tsp")
    