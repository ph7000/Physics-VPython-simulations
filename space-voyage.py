########################################################################
##                                                                        
##         DO NOT RUN THIS PROGRAM UNTIL YOU ARE ASKED TO DO SO 
##                          IN THE INSTRUCTIONS 
## 
########################################################################
from __future__ import division, print_function
from visual import *
scene.width =800
scene.height = 800


#CONSTANTS
G = 6.7e-11         # Gravitational constant (kg m**2/kg**2)
mEarth = 6e24     # Mass of Earth (kg) 
mcraft = 15e3       # Mass of spacecraft (kg)
deltat = 60            # Timestep for iterative calculation (s)

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6, color=color.yellow)

vcraft = vector(0,2e3,0)
pcraft = mcraft*vcraft


trail = curve(color=craft.color)    # create a trail to show trajectory of the craft

t = 0

#ITERATIVE CALCULATIONS
while t < 10*365*24*60*60:
    rate(100)                   # animation rate (frames/second)
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    trail.append(pos=craft.pos)  # add new position of the spacecraft to the trail
    r = (Earth.pos - craft.pos)
    rmag = math.sqrt(r.x**2 + r.y**2 + r.z**2)
    r = r/rmag
    F = r*(G*mEarth*mcraft)/(rmag**2)
    pcraft = pcraft + F*deltat
    t = t+deltat

