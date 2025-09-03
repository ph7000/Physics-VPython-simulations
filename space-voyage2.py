from __future__ import division, print_function
from visual import *

scene.width =800
scene.height = 800


#CONSTANTS
G = 6.7e-11         # Gravitational constant (kg m**2/kg**2)
mEarth = 6e24     # Mass of Earth (kg) 
mcraft = 15e3       # Mass of spacecraft (kg)
deltat = 100            # Timestep for iterative calculation (s)
mMoon = 7.0e22

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(1.01*Earth.radius, 0,0), radius=1e6, color=color.yellow)

Moon = sphere(pos=vector(4.0e8,0,0), radius=1.75e6, color=color.white)

vcraft = vector(1.30e4,0,0)
pcraft = mcraft*vcraft


trail = curve(color=craft.color)    # create a trail to show trajectory of the craft

t = 0

#ITERATIVE CALCULATIONS
while t < 60*24*60*60:
    rate(1000)                   # animation rate (frames/second)
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    trail.append(pos=craft.pos)  # add new position of the spacecraft to the trail
    trail.append(pos=Moon.pos)
    
    r = (Earth.pos - craft.pos)     #calculate r for earth and craft
    rMoon = (Moon.pos - craft.pos)      
    rMoonmag = mag(rMoon)       
    rMoon = rMoon/rMoonmag
    rmag = mag(r)
    if rmag < Earth.radius:     
        break
    if rMoonmag < Moon.radius:
        break
    r = r/(rmag)
    F = r*(G*mEarth*mcraft)/(rmag**2) + rMoon*(G*mMoon*mcraft)/(rMoonmag**2)        #calculate Fg between craft and moon and earth.
    pcraft = pcraft + F*deltat      #update p for iterations
    t = t+deltat    #update t for iterations

print(t/3600) #print time in hours
print(pcraft/mcraft)    #print final velocity
