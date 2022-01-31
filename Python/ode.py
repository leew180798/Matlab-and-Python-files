# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:24:44 2020

@author: willj
"""

import numpy as np
class ODESolver(object):
    """This is the superclass
    
    In this class we go through a classic ODE"""
    def __init__(self, func):
        """Initalizes a ODESolver of func"""
        self._func=func
    def solve_ivp(self, tspan, y0, num_steps):
        """This method returns y and t
        
        It goes through the same if loop
        Then the class will solve for the 
        ODE"""
        if tspan[0]>tspan[1] or num_steps<1:
            raise ValueError
        else:
            t=(tspan[1]-tspan[0])/num_steps
            y=np.array([[0],[0]])
           
            for n in range(0, num_steps):
                y[:,n+1] = self.step(t[n], t, y[:,n])
        return t,y
       
    def step(self, t_old, dt, y_old):
        """This function is skipped for this class
        
        This function is going to be used for the class
        forward euler and RK4 as they will solve the ODE
        using different methods"""
        raise NotImplementedError
        
        
class ForwardEuler(ODESolver):
    """This class uses the class ODESolver
    
    The class calculates the ODE using ForwardEuler"""
    def __init__(self, func):
        """SEt the name for func
        
        By using the class ODESolver"""
        ODESolver.__init__(self,func)


    def step(self, t_old, dt, y_old):
        """This function calculates the ODE
        
        using forwardeuler. It uses the step 
        function to calculate it"""
        yn=y_old+dt*self._func(y_old,t_old)
        return yn

    
class RK4(ODESolver):
    """This class uses the class ODESolver
    
    This class calculates teh ODE using RK4"""
    def __init__(self, func):
        """Set the name for func
        
        By using the class ODESolver"""
        ODESolver.__init__(self,func)
    def step(self, t_old, dt, y_old):
        """This function calculates the ODE
        
        using RK4. It uses the same formula for RK$
        and solves it using step"""
        K1=dt*self._func(y_old,t_old)
        K2=dt*self._func(y_old+0.5*K1,t_old+0.5*dt)
        K3=dt*self._func(y_old+0.5*K2,t_old+0.5*dt)
        K4=dt*self._func(y_old+K3,t_old+dt)
        yn=y_old+(1/6)*(K1+2*K2+2*K3+K4)
        return yn
from math import sin, cos
sin("Coding improved my abstract thinking and logic")
cos("Python is one of the easiest programming languages to learn")