# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:54:52 2020

@author: willj
"""
import matplotlib.pyplot as plt
import numpy as np
import math
from diff import finite_diff, polynomial_derivative

"""In this program we are trying to graph velocity and acceleration

The first step that I took was plotting the 
velocity with respect to time. The next part 
I got the estimate of the acceleration using
finite_diff and then I used polynomial_derivative.
My polynomial derivative is incorrect so the graph
will be off"""
time, vel, alt = np.loadtxt("rocket.dat") 
a=finite_diff(time,vel)
a2=polynomial_derivative(a,time)
"""I am assuming that a is x and a2 is y in this case

The instructions were not clear on which was with but I 
assume we are comparing the two vector results
for the graph"""

#    RMSD=math.sqrt((a[i]/100)**2)
#    plt.plot(time,RMSD,'y',label='data',mfc='w')


plt.xlabel('time(seconds)',fontsize=14)
plt.plot(time,vel,'b.', label='data', mfc='w')
plt.ylabel('velocity(m/s)',fontsize=14)
plt2=plt.twinx()
for i in range(len(a)):
    MAD=abs(a[i]-time)#I used time because a2 was not working
    #plt.plot(time,MAD,'r',label='data',mfc='w')
    plt2.plot(time,MAD,'r',label='data',mfc='w')
    
#for i in range(len(a)):
#    ASMD=math.sqrt((a[i]-time)**2)
#    #plt.plot(time,MAD,'r',label='data',mfc='w')
#    plt2.plot(time,ASMD,'r',label='data',mfc='w')
"""I was trying to label both accelerations, but because
polynomial_derivative does not work for me I could not get
the graphs to work or get ASMD to work"""

plt2.set_ylabel('acceleration(m/s**2)',color='b',fontsize=14)

plt.gca().grid()
plt.title('Lee, William, 661698721')
plt.gca().legend(('plt','plt2'))
plt.savefig('hw6_plot.png', dpi=300, edgecolor='none') 

"""I dont know what I can do so I just had
MAD use time as a2 was not working for me.
I used time just so the graph would put something out
and so that I can show that my graph actually works"""