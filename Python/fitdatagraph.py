
import matplotlib.pyplot as plt
import numpy as np
from fitdata import calc_fit, eval_fit

time, vel, alt = np.loadtxt("rocket.dat") 

plt.plot()

plt.plot(xlow,ylow)

plt.xlabel('time(seconds)',fontsize=14)
plt.ylabel('velocity(m/s)',fontsize=14)
plt.gca().grid()
plt.title('Lee, William, 661698721')
 
plt.savefig('hw4_plot.png', dpi=300, edgecolor='none') 