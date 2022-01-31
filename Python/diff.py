# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:04:24 2020

@author: willj
"""

import numpy as np
np.seterr(all='raise')
from math import factorial

def finite_diff(x,y):
    """THis function appromiximates teh dervitave using a finite difference
    
    The system goes through the foward difference and backwrard difference 
    to find the ends, while the central difference is used for inferior
    points"""
 
    if x.size!=y.size:
        raise ValueError
        print("Size of x or y are not the same")
    else:
        
        dydx=x.copy()
        try:
            dydx[0]=(y[1]-y[0])/(x[1]-x[0])
            dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
            for i in range(1,y.shape[0]-1):
                dydx[i]=(y[i+1]-y[i-1])/(x[i+1]-x[i-1])
            
            
        except FloatingPointError:
            print("x values must be unique")
            raise FloatingPointError
        else:
            return dydx

def polynomial_derivative(coef,x):
    """For this function it does a derivative of a polynomial
    
    This function goes through the horners method by going
    through the left and then to the right. The method
    comes from the description of the HW. It seems that 
    it wants us to use this as the instructions were very
    confusing in what we had to do with horners method.
    I also made p==0 as the velocity should not equal 0"""
    
    if coef.size==0:
        raise RuntimeError
    else:
        
        try:
            n=coef.size
            p=0.0
            for i in range(n,-1):
                p=coef[i]+(x)
        except ValueError:
            print("Velocity function is zero")
            raise ValueError
            
        else:
            return p
def fd_formula(x,deriv=1):
    """The jupyter notebook didnt help. I have no idea 
    
    what it meant when initializing the right side. I tried 
    to follow it and this is it. This is all I can come up with"""
    if type(deriv) != int:
        raise TypeError
    if deriv<0:
        raise ValueError
    if deriv>x.size-1:
        raise ValueError
    else:
        
        A=np.copy(x)
        for i in range(A.size):
            A[i]=1
        
        for i in range(x.size):
            for j in range(1):
                A=np.power(x[i],1)
        
        c=np.linalg.solve(A,deriv)
    return c


    
