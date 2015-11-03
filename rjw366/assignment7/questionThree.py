'''
Created on Nov 3, 2015

@author: rjw366
'''
import numpy as np

def quesitonThree():
    rand30 = np.random.rand(10,3)
    closestTuple = ()
    for i in rand30:
        closestAmount = .5
        closestIndex = 0
        index = 0
        for j in i:
            if(np.absolute(.5 - j) < closestAmount):
                closestAmount = np.abs(.5 - j)
                closestIndex = index
            index = index + 1
        closestTuple = closestTuple + (closestIndex,)
    print(rand30[range(10),closestTuple])
        