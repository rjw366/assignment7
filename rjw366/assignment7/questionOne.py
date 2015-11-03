'''
Created on Nov 3, 2015

@author: rjw366
'''
import numpy as np

def quesitonOneA():
    array = np.zeros(5)
    tempArray = [0,0,0,0,0]
    for i in range(1,6):
        newSet = [i + (x*5) for x in range(3)]
        tempArray[i-1] = newSet
        array = np.array(tempArray)
    print (array)
    return array
    
def quesitonOneB(array):
    bArray = array[1::2]
    print(bArray)

def quesitonOneC(array):
    cArray = array[:, 1]
    print(cArray)
    
def quesitonOneD(array):
    dArray = array[1:3, 0:3]
    print(dArray)
    
def questionOneE(array):
    newArray = np.zeros(0)
    for list in array:
        for i in list:
            if i > 3 and i < 11:
                newArray = np.append(newArray, i)
    print(newArray)
        