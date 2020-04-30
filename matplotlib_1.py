# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:14:24 2020

@author: legomate
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,1)
y = x

plt.plot(x, y)
plt.ylabel('some numbers')

#define axis
plt.axis([0, 6, 0, 6])
plt.show()