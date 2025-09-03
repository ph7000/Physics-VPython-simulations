from __future__ import division, print_function
from visual import *

track = box(pos=vector(0.0,-0.05,0.0),size=(2.0,0.05,0.10),color=color.white) #create track
cart = box(pos=vector(-0.95,0.0,0.0),size=(0.10,0.04,0.06),color=color.orange) #create cart

mcart = 0.80 #set mass of cart to .80 kg
pcart = mcart*vector(4.0,0.0,0.0) #p of cart is mass times this velocity vector
print ('cart momentum =',pcart,'kg m/s') #print the cart's momentum

ball = sphere(pos=vector(-0.95,0.0,0.0),radius=.02,color=color.cyan) #create ball

mball = 0.20 #set mass of ball
pball = mball*vector(4.0,2.35,0.0) #initial p of ball is its mass times this velocity vector; initial x component is same as that of the cart because they initially move together 

deltat = 0.001 #set time increment
t = 0.00 #initial time is 0.00 s

rcart = vector(-0.95,0.0,0.0) #use initial position variables for cart and ball for ease in loop iteration
rball = vector(-0.95,0.0,0.0)

Fgball = mball*vector(0.0,-9.8,0.0) #the only force in the system is Fg of ball, and it is in the y component, reflecting the ball's mass times g.

while (rcart.x<0.95): #while loop for iterations of t, momentum of ball y component, position of ball, and position of cart x component.
    rate(100) #rate is at maximum
    
    cart.pos = rcart #set cart's position equal to rcart, so rcart can be changed in each iteration (this creates animation)
    rcart = rcart + (pcart/mcart)*deltat #position of cart (rcart) changes according to the following equation for momentum, change in t, and change in r.
    
    ball.pos = rball #set ball's position equal to rball for use in changing position
    pball.y = pball.y + Fgball.y*deltat #momentum of ball's y component must change according to the force acting on it by this equation which relates net force to change in momentum
    rball.x = rball.x + (pball.x/mball)*deltat #change position of cart each iteration with equation relation change in velocity and time to change in position
    rball.y = rball.y + (pball.y/mball)*deltat
    
    print(t) #print new time value for each loop
    t=t+deltat #set a new t value to update it
    
print('after the loop')
