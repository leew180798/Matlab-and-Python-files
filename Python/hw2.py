import numpy as np
from math import pi, sin, cos
#u=np.array([1,2,3])
#v=np.array([1,2,3])


def dot_product(u,v):
    """Returns the dot product of vectors u and v.
    
    Given both vectors of u and v, dot_product computes the dot product by 
    computing the size of the vector and multiplying the vectors of the same axis.
    Then the system will add up the values and return the dot product."""
    dot=0.0
    for i in range(3):
        dot+=u[i]*v[i]
    return dot


def cross_product(u,v):
    """Returns the cross products of vectors u and v.
    
    This method implements the basic formula of solving a 3x3 vector. Using this formula
    the system computes the value for the x,y,z value of the vector and returns a 1x3 
    vector"""

    cross=[(u[1]*v[2])-(u[2]*v[1]),
           (u[2]*v[0])-(u[0]*v[2]),
           (u[0]*v[1])-(u[1]*v[0])]
    return cross 
def lever_shaft(F, tx, ty, tz, b, c, Dx, Dy, Dz):
    """Returns the vector force acting at point O, F_O, returns the moment of the Force at 
    point O as a vector, M_O, and returns the vector moment of the Force F about the line OD 
    as a vector, M_OD
    
    The method starts off by finding any variables that would lead to any of the vector forces equaling
    zero. This was done using an if statement to find those circumstances. If the variables used do not make
    the vector forces equal to zero, this system will then use the else statement. In order to calculate the F_O
    vector, the F variable would have to be multiplied by cosine of the angle of the designated axes. This will 
    return an F_O as a 1x3 matrix. Next, the M_O will be calculated by using the force vector and distance b and c.
    The system will multiply the distance and the F_O variables in a 3x3 matrix. The system will do it in the same
    method used inthe cross_product. Finally, M_OD will be calculated using the same method as M_O, using Dx,Dy, and 
    Dz variables for distance instead of b and c. The system will multiply the system as a 3x3 matrix."""

    t=np.array([tx,ty,tz])
    u=np.array([b,c,0])
    D=np.array([Dx,Dy,Dz])
    t=t*(pi/180)
    Fx=F*cos(t[0])
    Fy=F*cos(t[1])
    Fz=F*cos(t[2])
  
    if F==0.0:
        F_O=np.zeros(3)
        M_O=np.zeros(3)
        M_OD=np.zeros(3)
    else:
        F_O=np.array([Fx,Fy,Fz])
    if ((180<t[0] or t[0]<0.0) or (180<t[1] or t[1]<0.0) or (180<t[2] or t[2]<0.0)):
        F_O=np.zeros(3)
        M_O=np.zeros(3)
        M_OD=np.zeros(3)
    else:
        M_O=cross_product(u,F_O)
    if (Dx==0.0 and Dy==0.0 and Dz==0.0):
        M_OD=np.zeros(3)
    else:
        magD=dot_product(D,D)**0.5
        eD=D/magD
        M_OD=dot_product(eD,M_O)*eD
    
    
    return F_O, M_O, M_OD
    