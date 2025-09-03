from __future__ import division, print_function
from visual import *

# constants

G = 6.7E-11 # N*m^2/kg^2

mcraft = 15E3 # kg
mplanet = 6.0E24 # kg
scalefactor = 35000

planet = sphere(pos=vector(0,0,0),radius=6.4E6,color=color.cyan)
rcraftx = -13E7



while rcraftx < 13.1E7:
    craft = sphere(pos=vector(rcraftx,6.5E7,0.0),radius=3E6,color=color.yellow)
    
    r = planet.pos - craft.pos
    print(r)
    rmag = math.sqrt((r.x**2+r.y**2+r.z**2))
    print(rmag)
    Fmag = (G*mcraft*mplanet)/(rmag**2)
    print(Fmag)
    rhat = r/rmag
    print(rhat)
    Fnet = rhat*Fmag
    print(Fnet)

    
    rcraftx = rcraftx + 6.5E7
    Fvector = arrow(pos=craft.pos,axis=scalefactor*vector(Fnet.x,Fnet.y,Fnet.z),color=color.yellow)

 
