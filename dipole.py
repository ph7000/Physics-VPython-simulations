from __future__ import division, print_function
from visual import *

# Define constants

e = 1.6e-19         # charge of a proton, in C
ke = 9e9              # 1 / (4*pi*epsilon0), in N*m^2/C^2
scalefactor = 1e-17   # for E-field arrows (to be determined)
A2m = 1e-10      # conversion factor from Angstroms to meters
s = 4*A2m           # distance between + and - charge in dipole
R = 20*A2m        # radius of circle on which observation points are located
N=12                    # number of observation points

# Create objects

xaxis = cylinder(pos=vector(-30,0,0)*A2m, axis=vector(60,0,0)*A2m, radius=0.2*A2m)
yaxis = cylinder(pos=vector(0, -30,0)*A2m, axis=vector(0,60,0)*A2m, radius=0.2*A2m)
zaxis = cylinder(pos=vector(0,0,-30)*A2m, axis=vector(0,0,60)*A2m, radius=0.2*A2m)

rplus = vector(s/2,0,0)
rminus = vector(-s/2,0,0)

plus = sphere(pos=rplus, radius=s*0.2, color=color.red)
minus = sphere(pos=rminus, radius=s*0.2, color=color.blue)
plus.q = e
minus.q = -e

# Initial values

theta2 = 0.
theta = (2*pi)/N
robs = vector(0., 0., 0.)

# Calculations

while theta2 < 2*pi:
    robs.x = R*cos(theta2)
    robs.y = R*sin(theta2)
    r1 = robs-rplus
    r1mag = mag(r1)
    r1hat = r1/r1mag
    Efield1 = (ke)/(r1mag**2)*(r1hat)*plus.q
    r2 = robs-rminus
    r2mag = mag(r2)
    r2hat = r2/r2mag
    Efield2 = (ke)/(r2mag**2)*(r2hat)*minus.q
    Efield = Efield1 + Efield2
    Earrow = arrow(pos=robs, axis=Efield*scalefactor, color=color.orange)
    print('The electric field is ', Efield)
    theta2 = theta2 +theta
    
