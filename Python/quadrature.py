# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:10:00 2020

@author: willj
"""
import numpy as np

def midpoint(fvals, dx):
    """This function returns the midpoint

    It does this by checking that dx is <=0.
    Then it multplies the fvals by dx by the 
    one dimensional numpy array"""
    
    if dx<=0:
        raise ValueError
    else:
        midpoint=0.0
        for i in range(fvals.size):
            midpoint+=fvals[i]*dx
            
        
    return midpoint

def trapezoidal(fvals,dx):
    """This function returns the area
    
    This function makes sure dx<0 and then
    it goes through a for loop to get the total
    area of the given boundaries of Fx"""
    if dx<0:
        raise ValueError
    else:

        n=fvals.size
    
        area=(dx/2)*(fvals[0]+fvals[n-1])
        
        for i in range(1,n-1):
            
   
            area+= (dx/2)*(2*fvals[i])
            
    return area
        
def gauss_quad(func, numpts, a=-1, b=1):
    '''Gauss-Legendre quadrature of function over [a,b]

    Integrates user provided `func` over the interval [a,b] using
    Gauss-Legendre quadrature with `numpts` nodes for function
    evaluations.  Only 1 <= numpts <= 3 is supported.
    
    Input:  func   -- function to integrate
            numpts -- number of nodes
            a      -- lower bound of integral
            b      -- upper bound of integral
    '''
#     test input for a <= b
#     (add code)
    if a>b:
        raise ValueError 
    if numpts<1:
        raise ValueError
    if numpts>3:
        raise ValueError

    # define the quadrature nodes and weights
    if numpts == 1.0:
        xpts = np.array([0.0])
        wgts = np.array([2.0])
        n=np.size(xpts)
    elif numpts == 2.0:
        xpts = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
        wgts = np.array([1.0, 1.0])
        n=np.size(xpts)
    elif numpts == 3.0:
        xpts=np.array([0.0,-np.sqrt(3/5),np.sqrt(3/5)])
        wgts=np.array([(8/9),(5/9),(5/9)])
        n=np.size(xpts)
    else:
        raise ValueError
        
    # define the modifiers to the nodes and weights
    c0 = (b+a)/2
    c1 = (b-a)/2

    # apply quadrature formula
    integral=0.0
    for i in range(n):
        integral+=(wgts[i]*c1)*(func((c0+c1*xpts[i])))
    """I have tried so many little things out to get the right answer
    I put in the modifier and I put the modifiers in the integral as it 
    showed in the equation. I have no idea whats going on and this 
    is the best I can do with this lecture"""
    
    return integral

