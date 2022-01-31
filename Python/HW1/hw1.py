from math import sin, cos, pi
from angles import theta

thirty=(pi/6)
sixty=(pi/3)
f=500
side2=3**(1/2)
angle=(theta*(pi/180))
#print(angle)

rx=10*sin(30)*cos(60)
#print(rx)
ry=10*sin(30)*sin(60)
#print(ry)
rc=((f*rx*sin(angle))+(f*ry*cos(angle)))/10
ra=(f*sin(angle))-(125*(sin(angle)+side2*cos(angle)))
#print(ra)
T_BC=-250*(sin(angle)+side2*cos(angle))
print(T_BC)


T_AB=-((750*side2*sin(angle))-750*cos(angle))/3
print(T_AB)
T_AC=((1125*cos(angle))+(375*side2*sin(angle)))/3
print(T_AC)