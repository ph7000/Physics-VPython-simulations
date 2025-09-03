from __future__ import print_function, division
from visual import *

## constants

g = 9.8    # N/kg
mball = 0.2     # kg
L0 = 0.11       # m, natural length of the spring
k = 15.0        # N/m, spring constant
# uncomment and complete the code on the next line

# period =
tmax = 5.0      # s, change to an appropriate multiple of the period
deltat = 0.01    # s, change to an appropriate fraction of the period

## objects

ceiling = box(pos=(0,0,0),size=(0.2,0.01,0.2)) # origin is at ceiling
ball = sphere(pos=(0,-L0,0),radius=0.025,color=color.yellow)
spring = helix(pos=ceiling.pos,color=color.orange,radius=0.015,coils=40,thickness=.003)

spring.axis = ball.pos - ceiling.pos # spring is initially relaxed
ballposi = vector(0,-L0,0)

## initial values
pball = mball*vector(0,0,0)

## improve the display

scene.autoscale = 0 # camera won't zoom in and out
scene.center = vector(0,-L0,0) # move camera down
scene.range = vector(3*L0,3*L0,3*L0) # set range of display
scene.mouse.getclick() # animation starts when you click

## calculations inside a loop (i.e., repetetive calculations)

t = 0.0 # s, start counting time at zero

while t < tmax-0.5*deltat:
    rate(100)
    s = mag(spring.axis)-L0
    ## calculate force on ball by spring (note: requires calculation of L vector)
    Fmag = 1*k*(s)
    F = Fmag*spring.axis
    ## calculate net force on ball (note: has two contributions)
    Fnet = vector(0,-mball*g,0)+F
    ## apply momentum principle
    pball = pball + Fnet*deltat
    ## update position
    ball.pos = ball.pos + (pball/mball)*deltat
    ## update axis of spring
    spring.axis = ball.pos - ceiling.pos
    ## update time
    t = t + deltat
