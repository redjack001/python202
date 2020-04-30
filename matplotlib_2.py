# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:17:58 2020

@author: legomate
"""

import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
x = np.arange(0, 25, 1)

# red dashes, blue squares and green triangles
plt.plot(x, x/2, 'r--', x, x**2, 'bs', x, x**3, 'g^')
plt.show()

plt.ylabel('some numbers')
plt.grid(True)


