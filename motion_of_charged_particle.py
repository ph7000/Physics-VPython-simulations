from __future__ import division, print_function
from visual import *

# Define constants

e = 1.6e-19         # charge of a proton, in C
ke = 9e9              # 1 / (4*pi*epsilon0), in N*m^2/C^2
scalefactor = 1e-18   # for E-field arrows (to be determined)
A2m = 1e-10      # conversion factor from Angstroms to meters
s = 4*A2m           # distance between + and - charge in dipole
deltat = 1.0e-15
tf = 1.0e-11
t = 0
m = 1.67e-27 # mass of proton

# Create objects and initial values

xaxis = cylinder(pos=vector(-30,0,0)*A2m, axis=vector(60,0,0)*A2m, radius=0.2*A2m)
yaxis = cylinder(pos=vector(0, -30,0)*A2m, axis=vector(0,60,0)*A2m, radius=0.2*A2m)
zaxis = cylinder(pos=vector(0,0,-30)*A2m, axis=vector(0,0,60)*A2m, radius=0.2*A2m)

rplus = vector(s/2,0,0)
rminus = vector(-s/2,0,0)

plus = sphere(pos=rplus, radius=s*0.2, color=color.red)
minus = sphere(pos=rminus, radius=s*0.2, color=color.blue)
plus.q = e
minus.q = -e

robs=vector(0., 20., 0.)*A2m
proton = sphere(pos=robs, radius=s*0.2, color=color.magenta)
proton.q = e
p=m*vector(0.,0.,0.)

trail = curve(color=color.magenta)

# Calculations

while t < tf:
    rate(1000)
    robs=proton.pos
    r1 = robs-rplus
    r1mag = mag(r1)
    r1hat = r1/r1mag
    Efield1 = (ke)/(r1mag**2)*(r1hat)*plus.q
    r2 = robs-rminus
    r2mag = mag(r2)
    r2hat = r2/r2mag
    Efield2 = (ke)/(r2mag**2)*(r2hat)*minus.q
    Efield = Efield1 + Efield2
    p = p + (Efield*proton.q)*deltat
    proton.pos = proton.pos + p/m*deltat
    trail.append(proton.pos)
    t = t + deltat
    
print('The electric field is ', Efield)
    
