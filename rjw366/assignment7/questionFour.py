'''
Created on Nov 3, 2015

@author: ds-ga-1007
'''
import numpy as np
import matplotlib.pyplot as plt
from numpy import NaN

def quesitonFour():
    #Setup range of values
    x = np.arange(-2, .5, .005)
    y = np.arange(-1,  1, .005)
    z = np.zeros((len(x), len(y)))
    
    #For all values compute Mandelbrot
    for indexX, xVal in enumerate(x):
        for indexY, yVal in enumerate(y):
            z[indexX,indexY] = mandelbrotFunction(xVal,yVal)
    
    #Plot result
    plt.imshow(z.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
            
def mandelbrotFunction(x,y):
    """
    Takes x,y computes the resulting complex number and mandelbrot iteration
    """
    N_max = 50
    some_threshold = 50
    
    c = x + 1j*y
    
    z = c
    for v in range(N_max):
        z = z**2 + c
        if(abs(z) > some_threshold):
            return v
    return NaN
        