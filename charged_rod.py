from __future__ import division, print_function
from visual import *

# Define constants
e = 1.6e-19         # charge of a proton, in C
ke = 9e9              # 1 / (4*pi*epsilon0), in N*m^2/C^2
scalefactor = 5e-5   # for E-field arrows (to be determined)

L = 1.                    # length of rod, in m
Q =  5.8e-8                # total charge on rod, in C
N = 100.                    # number of point charges used to model rod
deltax = L/N          # length of each segment
deltaQ = Q/N      # charge of each segment

# Create objects

xaxis = cylinder(pos=vector(-0.75,0,0), axis=vector(1.5,0,0), radius=0.005)
yaxis = cylinder(pos=vector(0, -0.75,0), axis=vector(0,1.5,0), radius=0.005)
zaxis = cylinder(pos=vector(0,0,-0.75), axis=vector(0,0,1.5), radius=0.005)

x = vector(-L/2+deltax/2,0,0)  # x position of first point charge 
while x.x < L/2 :
    # display sphere to represent ith point charge
    sphere(pos=x, radius=.01, color=color.cyan)
    # calculate x for next point charge
    x.x = x.x +deltax

# Initial values
Do = 0.0
deltad = 0.1
Enet = vector(0., 0., 0.)

#improve display
scene.autoscale = 0 # camera won't zoom in and out
#scene.center = vector(4*L0,0,0) # move camera over
#scene.range = vector(6*L0,3*L0,3*L0) # set range of display

# Calculations

x = vector(-L/2+deltax/2,0,0)  # x position of first point charge 

while Do < 6.0 :
    robs = vector(Do, Do, 0)
    # Print and display net E field
    x = vector(-L/2+deltax/2,0,0)
    Enet = vector(0., 0., 0.)
    while x.x < L/2 :
        # Calculate E field due to point charge representing current segment
        r = robs - x
        Efield = ke*deltaQ/(mag(r)**2)*(r/mag(r))
        # Add this contribution to Enet
        Enet = Enet + Efield
        # update x
        x.x = x.x +deltax
    print ('Net E field:', Enet)
    arrow(pos=robs, axis=Enet*scalefactor, color=color.orange)
    print ("d:", Do)
    print ("robs mag:", mag(robs))
    theta = (atan(Enet.y/Enet.x))*180/pi
    print ("theta:", theta)
    Do= Do + deltad
    


    
