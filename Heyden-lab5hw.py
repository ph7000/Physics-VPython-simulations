from __future__ import division, print_function
from visual import *

## Constants
mu0over4pi = 1*10e-7 #mu naught over 4 pi
A2m = 1e-11 #A scalefactor for the axes (not actually Angstroms)
qproton = 1.6e-19 #charge of proton in coulombs
scale = 2.0e2 #note: this scale, which controls the arrows' size, is tailored for the end of the calculation, and thus might be too large while the motion is occurring

# In this section, define any constants you may need

## Objects

xaxis = cylinder(pos=vector(-50.,0.,0.)*A2m, axis=vector(100.,0.,0.)*A2m, radius=0.2*A2m)
yaxis = cylinder(pos=vector(0.,-50.,0.)*A2m, axis=vector(0.,100.,0.)*A2m, radius=0.2*A2m)
zaxis = cylinder(pos=vector(0.,0.,-50.)*A2m, axis=vector(0.,0.,100.)*A2m, radius=0.2*A2m)

# Change the initial vector position of the protons below:
d = 8.0e-11 #m
proton = sphere(pos=vector(-4.0e-10,0,0), radius=1e-11, color=color.red)
proton2 = sphere(pos=vector(4.0e-10,d,0), radius=1e-11, color=color.red)

# Change the observation location (position of the tail of the arrow) below:
# Add more arrows to display the magnetic field at other observation locations.
# Set axis to (0,0,0) initially and update it in the loop.

barrow1 = arrow(pos=vector(0,d,0), axis=vector(0,0,0), color=color.cyan)
r1=vector(0.,0.,0.)
r1hat=vector(0.,0.,0.)
B1field=vector(0.,0.,0.)

barrow2 = arrow(pos=vector(0,-d,0), axis=vector(0,0,0), color=color.cyan)
r2=vector(0.,0.,0.)
r2hat=vector(0.,0.,0.)
B2field=vector(0.,0.,0.)

#barrow3 = arrow(pos=vector(0,0,d), axis=vector(0,0,0), color=color.cyan)
#r3=vector(0.,0.,0.)
#r3hat=vector(0.,0.,0.)
#B3field=vector(0.,0.,0.)

#barrow4 = arrow(pos=vector(0,0,-d), axis=vector(0,0,0), color=color.cyan)
#r4=vector(0.,0.,0.)
#r4hat=vector(0.,0.,0.)
#B4field=vector(0.,0.,0.)

## Initial values

velocity = vector(2.0e4,0,0) # Enter the proton's initial velocity
deltat = 1.0E-15 #1.0E-19 # Adjust if program runs too slowly or too quickly

scene.autoscale = 1 # Turns off autoscaling.  Set to 1 to turn it back on.

while proton.pos.x < 5.0E-10:
    rate = 1000

    proton.pos = proton.pos + velocity*deltat # Update the proton's position (this is at the beginning because the deltat is large)
    proton2.pos = proton2.pos + (-1)*velocity*deltat
    
    # For each magnetic field vector:
    barrow1.pos = proton2.pos #set the position of the arrow to the first proton's position 
    r1 = barrow1.pos - proton.pos  # 1. Calculate r and rhat
    r1mag = mag(r1)
    r1hat = r1/r1mag
    B1field = mu0over4pi*qproton*cross(velocity,r1)/(mag(r1)**2)  # 2. Calculate the magnetic field vector
    barrow1.axis = scale*B1field  # 3. Calculate the new axis of the arrow.  Scale it appropriately.

    barrow2.pos = proton.pos
    r2 = barrow2.pos - proton2.pos  # 1. Calculate r and rhat
    r2mag = mag(r2)
    r2hat = r2/r2mag
    B2field = mu0over4pi*qproton*cross(((-1)*velocity),r2)/(mag(r2)**2)  # 2. Calculate the magnetic field vector
    barrow2.axis = scale*B2field  # 3. Calculate the new axis of the arrow.  Scale it appropriately.

    #r3 = barrow3.pos - proton.pos  # 1. Calculate r and rhat
    #r3mag = mag(r3)
    #r3hat = r3/r3mag
    #B3field = mu0over4pi*qproton*cross(velocity,r3)/(mag(r3)**2)  # 2. Calculate the magnetic field vector
    #barrow3.axis = scale*B3field  # 3. Calculate the new axis of the arrow.  Scale it appropriately.

    #r4 = barrow4.pos - proton.pos  # 1. Calculate r and rhat
    #r4mag = mag(r4)
    #r4hat = r4/r4mag
    #B4field = mu0over4pi*qproton*cross(velocity,r4)/(mag(r4)**2)  # 2. Calculate the magnetic field vector
    #barrow4.axis = scale*B4field  # 3. Calculate the new axis of the arrow.  Scale it appropriately.

