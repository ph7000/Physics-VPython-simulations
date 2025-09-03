from __future__ import division, print_function
from visual import *

## CONSTANTS

km = 1e-7 # mu_0/4pi in units of Telsa*meter/Ampere
scalefactor = 1e5

current = 1 # current in Amps
a = 0.01 # radius of loop, in m
d = 0.05 # distance of observation points from origin, in m
Nseg = 4 # number of segments used to model loop
Nobs = 8 # number of observation locations

## OBJECTS

# create axes 
xaxis = cylinder(pos=vector(-10*a,0,0),axis=(20*a,0,0),radius=a*5e-2,color=color.white)
yaxis = cylinder(pos=vector(0,-10*a,0),axis=(0,20*a,0),radius=a*5e-2,color=color.white)
zaxis = cylinder(pos=vector(0,0,-10*a),axis=(0,0,20*a),radius=a*5e-2,color=color.white)

# create ring in x-y plane
loop = ring(pos=vector(0,0,0),radius=a,color=color.red,axis=vector(0,0,1))

# create lists containing the observation locations ...
# ... and arrows representing B field at those locations

robs = []
Barrow = []
iobs=0
deltaphi=2*pi/Nobs  
while iobs < Nobs:
    phi = iobs*deltaphi
    robs.append(vector(d*cos(phi),0,d*sin(phi)))
    Barrow.append(arrow(pos=robs[iobs],axis=vector(0,0,0),color=color.cyan))
    iobs = iobs + 1

## CALCULATIONS

# First loop through observation points

iobs = 0
dtheta = 2*pi/Nseg

while iobs < Nobs:
    
    theta = 0
    Bnet = vector(0,0,0)  # reset Bnet to zero for each observation point
    
    while theta < 2*pi:
        ri = robs[iobs] - a*vector(cos(theta),sin(theta),0)
        rihat = ri/mag(ri)
        dli = a*dtheta*vector(-sin(theta),cos(theta),0)
        dB = km*current*cross(dli,rihat)/(mag(ri)**2)
        Bnet = Bnet + dB
        theta = theta + dtheta
        
    ## Add lines to loop through segments, calculate Bfield due to ...
    ## ... each segment and add to Bnet

    Barrow[iobs].axis = Bnet*scalefactor
    iobs = iobs + 1
    print(Bnet)
