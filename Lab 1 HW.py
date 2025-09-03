from __future__ import division, print_function
from visual import *

n  =  3
dtheta = 2*pi/n     #unit circle value (division yields dtheta to provide 3 theta values between 0 and 2pi)

theta =  pi/3   #initial sphere unit circle theta value

r=0.2   #radius of unit circle

while (theta < 2*pi):   #loop to stop after three theta values (giving three spheres)
    
    print(theta*(180./pi))
    
    x=r*cos(theta)  #x component of sphere
    y=r*sin(theta)  #y component of sphere

    x1=r*cos(theta+dtheta)  #x component of adjacent sphere
    y1=r*sin(theta+dtheta)  #y component of adjacent sphere
    
    hi = sphere(pos=vector(x,y,0),radius=.05,color=color.green)     #current green sphere with position component x and y
    bye = arrow(pos=hi.pos,axis=vector(x1-x,y1-y,0),color=color.red)    #red arrow with vector connecting adjacent sphere to current sphere
    
    theta = theta + dtheta  #update theta value for next run through loop

print('all done!')
