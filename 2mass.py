from __future__ import print_function, division
from visual import *
from visual.graph import *

## constants
g = 9.8         # N/kg
m1 = .2       # kg
m2 = .1         # kg
L0 = .11        # m, natural length of the spring
k = 15.0        # N/m, spring constant
period = 2.*pi*sqrt(m2/k)
tmax = 10.*period       # s, change to an appropriate multiple of the 
period
deltat = 0.001*period   # s, change to an appropriate fraction of the 
period

## objects
b1 = sphere(pos=(0,0,0),radius=0.025,color=color.green)
b2 = sphere(pos=(0,-1.5*L0,0),radius=0.025,color=color.red)
spring = helix(pos=b1.pos,color=color.orange,radius=0.015,
coils=40,thickness=.003)
spring.axis = b2.pos - b1.pos
b1trail = curve(color=color.green)
b2trail = curve(color=color.red)
cmtrail = curve(color=color.white)
Egraph = gcurve(color=color.white)      # energy (K+U)
Kgraph = gcurve(color=color.red)        # total kinetic energy
Ugraph = gcurve(color=color.green)      # spring potential energy
Ktransgraph = gcurve(color=color.cyan)
Krelgraph = gcurve(color=color.magenta)

## initial values
p1 = vector(0.06,0.,0.)   # a vector (kg*m/s)
p2 = vector(-0.02,0.,0.)   # a vector (kg*m/s)

## improve the display
scene.autoscale = 0 # camera won't zoom in and out
scene.center = vector(4*L0,0,0) # move camera over
scene.range = vector(6*L0,3*L0,3*L0) # set range of display
scene.mouse.getclick() # animation starts when you click

## calculations inside a loop (i.e., repetetive calculations)
t = 0.0 # s, start counting time at zero
while t < tmax-0.5*deltat:
    rate(500)
    F1 = k*(b2.pos-b1.pos) ## calculate net force on each ball
    F2 = k*(b1.pos-b2.pos)
    p1 = p1 + F1*deltat ## apply the momentum principle
    p2 = p2 + F2*deltat
    spring.axis = b2.pos-b1.pos ## update the spring
    spring.pos = b1.pos
    b1.pos = b1.pos + (p1/m1)*deltat 
    b2.pos = b2.pos + (p2/m2)*deltat 
    b1trail.append(b1.pos) ## append the new positions of b1 and b2 to each trail
    b2trail.append(b2.pos)
    Ktotal = mag(p1)**2/(2*m1) + mag(p2)**2/(2*m2) ## compute energies and graph them
    Uspring = mag(F1)**2/(2*k)
    E = Ktotal + Uspring
    Kgraph.plot(pos=(t,Ktotal))
    Ugraph.plot(pos=(t,Uspring))
    Egraph.plot(pos=(t,E))
    rcm = 1/(m1+m2)*(m1*b1.pos + m2*b2.pos) ## determine the cm position and momentum
    pcm = p1 + p2
    cmtrail.append(rcm) ## append the new cm position to the cm trail
    p1rel = p1 - pcm ## compute momenta relative to the cm
    p2rel = p2 - pcm
    Ktrans = mag(pcm)**2/(2*(m1+m2))
    Krel = Ktotal - Ktrans ## compute Ktrans and Krel and graph them
    Ktransgraph.plot(pos=(t,Ktrans))
    Krelgraph.plot(pos=(t,Krel))
    t = t + deltat ## update time
