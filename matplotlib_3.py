# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:19:53 2020

@author: redjack001
"""
import matplotlib.pyplot as plt
import numpy as np


names = ['A', 'B', 'C', 'D']
values = np.arange(0,4,1)
values2 = np.arange(0,2,0.5)
print(values)

plt.figure(figsize=(12, 5))

#plot 1
plt.subplot(141)
plt.bar(names, values)
plt.xlabel('Bar Chart')

#plot 2
plt.subplot(142)
plt.scatter(names, values)
plt.xlabel('Scattered Diagram')

#plot 3
plt.subplot(143)
plt.plot(names, values)
plt.xlabel('Simple Plot')

#plot4
plt.subplot(144)
plt.plot(names, values, 'gs-', values2, 'r--')
plt.xlabel('2 Variables')

#overall title
plt.suptitle('Categorical Plotting')
plt.show()