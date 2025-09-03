from __future__ import division, print_function
from visual import *

print("Shows E inside and outside line of charged rings representing a wire")
print("Click in graphic display window to show E field vectors")

# Constants
ke = 9.E9

N = 40      # number of rings
L = 0.05    # length of wire in meters
dL = L/N    # distance between rings
ring_radius = 1.E-3 # radius of each ring in meters
Q = 1.E-9   # maximum charge on each ring, in Coulombs

Nobs = 10   # number of y-z observation planes along the length of wire
Lobs = L/2. # length (in x) of the observation region
dLobs = Lobs/Nobs # spacing between observation planes
# y coordinates of each observation point
yobs = [-1.3*ring_radius, -0.7*ring_radius, -0.3*ring_radius,
         0.3*ring_radius,  0.7*ring_radius,  1.3*ring_radius]

scalefactor = 2.E-10

###

# Define a function that creates a list of spheres representing point charges
# in a ring.  Spheres are colored according to their charge: blue, white, red
# for negative, zero, positive, respectively.

def qring(rradius=10, nptcharges=20, totalq=1e-9, xx=0):

    dq = totalq/nptcharges
    dtheta = 2.*pi/nptcharges

    qcolor = color.white
    if (totalq < 0.):
        qcolor = color.blue
    elif (totalq > 0.):
        qcolor = color.red

    thisring = []
    for theta in arange(0.,2.*pi,dtheta):
        aa = sphere(pos=(xx,rradius*sin(theta),rradius*cos(theta)),radius=rradius/15.)
        aa.q = dq
        aa.color = qcolor
        thisring.append(aa)

    ring(pos=(xx,0,0),axis=(1,0,0),radius=rradius,thickness=rradius/75.,color=qcolor)

    return thisring

###

rings = []          # list of rings (empty to start)
ring_charge = []    # list of total charge/ring (empty to start)

# ADD CODE HERE TO CUSTOMIZE THE CHARGE DISTRIBUTION

ring_charge = [-Q]
c = 0 #counter
m = 2*Q/(N-1) #slope iterated
charge = -Q
while c<(N-1):
    charge=charge+m
    ring_charge.append(charge)
    c=c+1

ring_charge.append(Q)

# READ AND UNDERSTAND WHAT THE REMAINING CODE DOES

x = -L/2. + dL/2.
for i in range(N):  # append ith ring to the list of rings
    rings.append(qring(rradius=ring_radius,nptcharges=20,totalq=ring_charge[i],xx=x))
    x = x + dL
    
scene.mouse.getclick()  # pause at this line until the mouse is clicked
for ring in rings:
    for ptq in ring:
        ptq.visible = not(ptq.visible)

x = -Lobs/2. + dLobs/2.
for i in range(Nobs):   # loop over x coordinate of the observation points
    for y in yobs:          # loop over y coordinates
        robs = vector(x,y,0.)
        E = vector(0.,0.,0.)
        for ring in rings:      # loop over rings
            for ptq in ring:        #  loop over point charges in each ring
                r = robs - ptq.pos
                E = E + (ke*ptq.q/mag(r)**2)*(r/mag(r))
        arrow(pos=robs,axis=E*scalefactor,color=color.orange,shaftwidth=ring_radius/20.) 
    x = x + dLobs
print(mag(E))
while 1:
    scene.mouse.getclick()
    for ring in rings:
        for ptq in ring:
            ptq.visible = not(ptq.visible)
