import numpy as np
"""This module extracts data to find the best fit data

It goes through calc fit and then
it goes through eval fit in order to find
the best point
"""

def calc_fit(xdata,ydata,degree=1):
    
    """This function returns 
    
    the coeff that define the polynomial
    First the system goes through assert 
    statements to make sure it
    meets the requirements. Then the 
    system goes through the array. 
    Then the values each go through a 
    QR decomposition
    """
    
    assert degree>=0
    assert len(xdata.shape)==1
    assert xdata.shape == ydata.shape

    x_coeff=degree+1
    x=len(xdata)
    x2=np.ones([x,x_coeff])
    
    for i in range(1,x_coeff):
        x2[:,i]=(x2[:,i-1]*xdata)
    q,r=np.linalg.qr(x2)
    qty=q.T@ydata
    coeff=back_sub(r,qty)
    return coeff

def eval_fit(coeff, x):
    
    """This system returns the array 
    
    of locations that would best fit
    In order to do this the polynomial it goes through 
    the element of x and coeff in the i 
    and then j using a for loop. 
    After this the system adds
    """ 
    
    z=x.size
    y=np.zeros(z)
    z2=coeff.size
    
    for i in range(z):
        y[i]=coeff[0]
        exp=1
        for j in range(1,z2):
            y[i]+=coeff[j]*(x[i]**exp)
            exp+=1
    return y
    
def back_sub(U,b):
    
    """Returns decomposition of the U matrix.
    
    This method uses for loop to go through 
    each column in order to get the upper 
    and lower matrix
    """

    z=np.zeros(b.size)

    for i in range(b.shape[0]-1,-1,-1):
        z[i]=b[i]*(1/U[i,i])
        for j in range(i+1,b.shape[0]):
            z[i]-=(U[i,j]*z[j])*(1/U[i,i])
    return z


