from __future__ import division, print_function
from visual import *

##constants
N = 401.
L = 1.
R = 4.*L/N
deltax = R/4.
x = vector(-L/2,0,0)
rope = []

w = 20.*R 
A = 1.e6
v=2.
t=0.
deltat=.01
z=0.

##creating rope using append
while x.x <= L/2:
    ball = sphere(pos=x, radius=R, color=color.cyan)
    rope.append(ball)
    x.x=x.x+deltax

##define wave
def wave (z):
    if z<0 or z>w:
        y=0
    else:
        y=A*z*z*z*z*z*(w-z)*(w-z)
    return y;   

##for loop nested inside while loop
while t<L/v: #while loop updates time
    rate(10)
    for ball in rope:
        ball.pos.y=wave(ball.pos.x+v*t-L/2+.5*w)-wave(ball.pos.x-v*t+L/2)
        #the ball's y position is updated at a function of time.  At t=0,
        # the upright wave's x value is at L/2, the inverted wave's at -L/2.
    t=t+deltat
