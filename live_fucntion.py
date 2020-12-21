from math import *
import matplotlib.pyplot as plt
import numpy as np


a = #it depend on your pc
x = np.linspace(0, 10, a)

def function(x):
    s = #your function
    return(s)

fig = plt.figure()
plt.ion()

i = 0

while i < a:
    xf = x[i]
    plt.scatter(xf, function(xf), color = 'blue')
    i = i+1
    plt.pause(0.0001)
