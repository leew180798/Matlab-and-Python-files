import numpy as np
from math import sin, cos, pi
import linsolve
def truss(angle, load):
    
    """truss finds the force of tension
    
    truss takes the array / 'load' array and fixes the rows to use LU decomposition. 
    Then they are entered into linsolve to produce the array to its original state
    """
    
    ang = angle*(pi/180)
    c = cos(ang)
    s = sin(ang)
    
    G = np.array([[ s,  0, -s, -1,  0,  0,  0,  0,  0,  0,  0],
                  [-c,  0, -c,  0,  0,  0,  0,  0,  0,  0,  0],
                  [ 0,  1,  s,  0, -s, -1,  0,  0,  0,  0,  0],
                  [ 0,  0,  c,  0,  c,  0,  0,  0,  0,  0,  0],
                  [ 0,  0,  0,  1,  s,  0, -s, -1,  0,  0,  0],
                  [ 0,  0,  0,  0, -c,  0, -c,  0,  0,  0,  0],
                  [ 0,  0,  0,  0,  0,  1,  s,  0, -s, -1,  0],
                  [ 0,  0,  0,  0,  0,  0,  c,  0,  c,  0,  0],
                  [ 0,  0,  0,  0,  0,  0,  0,  1,  s,  0, -s],
                  [ 0,  0,  0,  0,  0,  0,  0,  0, -c,  0, -c],
                  [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  s]])
    G[[1,2]] = G[[2,1]]
    G[[3,4]] = G[[4,3]]
    G[[5,6]] = G[[6,5]]
    G[[7,8]] = G[[8,7]]
    G[[9,10]] = G[[10,9]]
    L = load.copy()
    L[[1,2]] = L[[2,1]]
    L[[3,4]] = L[[4,3]]
    L[[5,6]] = L[[6,5]]
    L[[7,8]] = L[[8,7]]
    L[[9,10]] = L[[10,9]]
    
    t = linsolve.solve(G,L)
    
    return t
def max_force(tension):
    
    """max_force returns the max value from tension
    -
    max_force goes through the tension array and checks each index for the
    largest value. It compares to the previous max and in the end returns the max
    """
    
    x=tension.shape[0]
    
    maxVal = 0
    
    for i in range(x):
        if abs(tension[i]) >= abs(maxVal):
            maxVal = (tension[i])
            max_in=i+1
        else:
            continue
            
    max1 = int(max_in)
    max2 = float(maxVal)
            
    return max1, max2