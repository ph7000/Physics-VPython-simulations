from __future__ import division, print_function
from visual import *

#constants
e = 1.6E-19 # C, fundamental unit of charge
ke = 9.0E9 # Coulomb's constant
A2m = 1.0E-10 # meters per Angstrom
scalefactor = 5.E-18

# create objects

xaxis = cylinder(pos=vector(-50.,0.,0.)*A2m, axis=vector(100.,0.,0.)*A2m, radius=0.2*A2m)
yaxis = cylinder(pos=vector(0.,-50.,0.)*A2m, axis=vector(0.,100.,0.)*A2m, radius=0.2*A2m)
zaxis = cylinder(pos=vector(0.,0.,-50.)*A2m, axis=vector(0.,0.,100.)*A2m, radius=0.2*A2m)

rsource = vector(0.,0.,0.)
ion = sphere(pos=rsource, radius=1.*A2m, color=color.yellow)
ion.q = -e #the ion's charge is negative one times the charge constant "e"

robs = vector(20.,0,0)*A2m #define initial observation position
r = 20.*A2m #define radius of observation circle

n = 12 #define the number of observation points along the circle
Nobs=1 #define a starting value for the number of observation points (increases each iteration)

theta = 2*pi/n #define an angle value theta representing the space between observation points
theta2 = 0 #define an initial value of theta so "theta" can be added to "theta2" each iteration (see end of loop)

while Nobs <=n:
    r = robs-rsource
    rmag = mag(r)
    rhat = r/rmag
    Efield = (ke)/(rmag**2)*(rhat)*e
    Earrow = arrow(pos=robs, axis=Efield*scalefactor, color=color.orange)
    print('The electric field is ', Efield)
    robs.y=r*sin(theta2)
    robs.x=r*cos(theta2)
    theta2 = theta2 +theta
    Nobs = Nobs +1

