"""A = 64.0
r = 0.999879
t = 0
while True:
    t += 1 # add to the year
    A *= r # update the amount
    if A<8.0:
        break
print("It will take",t,"years.")"""

def bisection(func,xlow,xupp,
              ftol=1e-12,
              xtol=1e-7,
              maxiter=100):
    """This funciton calculates the roots
    
    This is done by making sure the boundaries have the value.
    Then it will calculate the function by going through the beginning 
    and middle boundary, then the middle and upper boundary. After that,
    it will find the roots by going through a while loop. The assert
    statements make sure maxiter is within bounds, and makes sure
    the x bounds can be used. It also makes sure the brackets are not
    the roots"""
    fu=func(xupp)
    fl=func(xlow)
    
    xm=0.5*(xlow+xupp)
    fm=func(xm)
    iter=0.0
    
    assert xupp>xlow
    assert (fl*fu)!=0.0 
    #assert (fl*fu)<0.0
    assert maxiter>=1.0
    
    
    """if fl*fu==0.0:
        raise ValueError("Fault Root")
    elif fl*fu>0.0:
        raise ValueError("Error")"""
    while (abs(fm)>ftol) and (abs(xupp-xlow)>xtol) and (iter<maxiter):
        assert(fl*fu)<0.0
        if fl*fm<0.0:
            fu=fm
            xupp=xm
        elif fl*fm>0.0:
            fl=fm
            xlow=xm
        else:
            break
        xm=0.5*(xlow+xupp)
        fm=func(xm)
        iter+=1.0
        assert maxiter<=1000.0
    return xm 
        
     