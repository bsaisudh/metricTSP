# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:35:36 2019

@author: balam
"""

from generateRandomData import TSPfileWrite
from TSPFindTour import FindTSPTour


# =============================================================================
# for filename in ['eil51.tsp',
#           'eil76.tsp',
#           'eil101.tsp',
#           'test.tsp',
#           'test1.tsp',
#           'test2.tsp']:
#     FindTSPTour(f"Data/{filename}")
# 
# =============================================================================
for i in range (10):
    n = 2
    m = 300
    filename = f'{m}RandomPoints - {i}'
    TSPfileWrite(filename,n,m)
    FindTSPTour(f"Data/Random/{filename}.tsp")
    