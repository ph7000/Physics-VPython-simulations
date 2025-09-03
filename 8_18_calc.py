from __future__ import division, print_function
from visual import *

m = 2 #initial state of hydrogen
n = 3 #final state of hydrogen

E = (-13.6)/m**2 #initial Energy
Ef = 0 #Use loop to determine final energy

while m < n+.5:
    Ef = (-13.6)/m**2
    m = m+1

dE = Ef - E
print(dE)
    
