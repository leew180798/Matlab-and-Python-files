import numpy as np
from find_root import bisection  

import matplotlib.pyplot as plt

def bb_residual(P,V,T,AO,BO,a,b,c):
    """This system calculates the residual using 7 var.
    
    Using the equations given, everything is set equal to residual
    or zero. The residual is calculated using hte bridgeman
    equation. This will be used later to find V"""
    #intialize P vector
    #intialize z vector
    #Loop through P
        #then calculate V as a residual
        #calculate z[i]
    #plot result
    R=0.08205
    beta=(R*T*BO)-AO-((R*c)/T**2)
    gamma=-(R*T*BO*b)+(AO*a)-((R*BO*c)/T**2)
    delta=((R*BO*b*c)/T**2)
    residual=((R*T)/V)+(beta/(V**2))+(gamma/V**3)+(delta/V**4)-P
    return residual
#Lamda V:residual(P[i],V,T,AO,BO,a,b,c)
    
"""Using residual, z, compressibility factor, is calculated and plotted.

Using the values given. T is given as an array. P is an array using
200 values. This is put in a for loop to go through all the P values using
two T values. The residual function is used with the help of lambda.
Using the V, it is put in an equation to solve Z. Z is then plotted with two
lines with two different temperatures."""

T=np.array([273,473])
R=0.08205
P=np.linspace(1,200,200)

AO=2.27690
BO=0.05587
a=0.01855
b=-0.01587
c=128300

#z=zeros(len(P),len(T))
for i in range(len(T)):
    for j in range(len(P)):
        Ti=T[i]
        Pj=P[j]
        V=bisection(lambda x: bb_residual(Pj,x,Ti,AO,BO,a,b,c), 0.01, 100)
        #V=(R*Ti)/Pj
        #print(V)
        z=(Pj*V)/(R*Ti)
        if Ti==273:
            plt.plot(Pj,z, 'r.', label='data', mfc='w') #Temp of 273 data
        else:
            plt.plot(Pj,z, 'k.', label='data', mfc='w') #Temp of 472 data
        
plt.xlabel('Pressure (atm)', fontsize=14)
plt.ylabel('Z (Compressiblity Factor)', fontsize=14)
plt.title('Lee, William, 661698721')
plt.gca().grid() # add grid lines
plt.savefig('hw5_plot.png', dpi=300, edgecolor='none') 

        