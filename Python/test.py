import numpy as np
from math import sin, cos, pi
"""u=np.array([1,4,3])
v=np.array([5,2,7])
sum=0
#dot_product(u,v)
#print(dot_product(u,v))

        
#print(sum)

from hw2 import dot_product
print(dot_product(u,v))
from hw2 import cross_product
print (cross_product(u,v))
from hw2 import lever_shaft
print (lever_shaft(1,1,1,1,5,5,1,0,1))
"""
"""def qqq(x):   
    y=(x+1)*(x-1)
    return y
import find_root
root=find_root.bisection(qqq,0,4)
print(root)"""
import numpy as np

# --- Generate plot data -------------------------------------

npoints = 10                        # vary the number of points
x = np.linspace(-12, 12, npoints)
y = np.cos(x**2)

# --- Make the plot ------------------------------------------

import matplotlib.pyplot as plt
plt.figure(1, figsize=(6, 4))       # 6in x 4in figure

plt.plot(x, y, '-r', lw=2)          # plot the data as a line

plt.xlabel('x', fontsize=14)                     # label x axis
plt.ylabel('y(x) = cos(x**2)', fontsize=14)      # label y axis
plt.gca().grid()                    # add grid lines
plt.title("Illustration of Discretization Error")

plt.show()
print("    y(x) = x**4    y'(x) = 4*x**3    x = 1.0")
print()
print('     dx       exact       approx      error     rel err ')
print(' ---------- ---------- ----------- ---------- ----------')

x  = 1.0   ;   dx = 1.0

for i in range(0, 12):
    exact  = 4 * x**3
    approx = ( (x+dx)**4 - x**4 ) / dx
    err = approx - exact
    relerr = err/exact
    print('{:10.7f} {:10.7f}  {:10.7f}  {:10.7f}  {:7.1%}'.format(dx, exact, approx, err, relerr))
    dx /= 2.0
    
# f(x) = e**(-x)      f'(x) = -e**(-x)       x = 1.0
#
# forward difference
# backward difference
# centered difference
#
import numpy as np

n_tests = 11

dx     = np.zeros(n_tests)
err_fd = np.zeros_like(dx)
err_bd = np.zeros_like(dx)
err_cd = np.zeros_like(dx)
print(dx, err_fd)

x     = 1.0
exact = -np.exp(-x)

for i in range(0, n_tests):

    dx[i] = 10.0**(-i)

    approx = ( np.exp(-(x+dx[i])) - np.exp(-x) ) / dx[i]
    err_fd[i] = abs(approx - exact)

    approx = ( np.exp(-(x-dx[i])) - np.exp(-x) ) / (-dx[i])
    err_bd[i] = abs(approx - exact)

    approx = ( np.exp(-(x+dx[i])) - np.exp(-(x-dx[i])) ) / (2*dx[i])
    err_cd[i] = abs(approx - exact)

for i in range(0, n_tests):
    dx[i] = 10.0**(-i)
    print(i, dx[i], approx, err_fd[i], err_bd[i], err_cd[i])

# ----- Make Plot ---------------------------------------
    
import matplotlib.pyplot as plt
plt.figure(1, figsize=(6, 4))             # 6in x 4in figure

plt.loglog(dx, err_fd, '-r', label='2 pt forward difference', lw=1)        # plot the curve
plt.loglog(dx, err_bd, '-b', label='2 pt backward difference',lw=1)        # plot the curve
plt.loglog(dx, err_cd, '-g', label='3 pt centered difference',lw=2)        # plot the curve

plt.title("Absolute Error Estimating Derivative of y = exp(-x) at x = 1")
plt.xlabel('dx', fontsize=14)             # label x axis
plt.ylabel('error = |estimate - (-exp(-1))|', fontsize=14)    # label y axis
plt.legend(fontsize=12, loc=2) # add a legend
plt.gca().grid()                          # add grid lines

plt.show()                                # display the plot