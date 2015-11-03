'''
Created on Nov 3, 2015

@author: rjw366
'''
import numpy as np

def quesitonTwo():
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    divided = np.transpose(a)/b
    print(np.transpose(divided))
    
        