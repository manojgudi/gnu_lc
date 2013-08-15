#!/usr/bin/python -tt

from matplotlib.pyplot import * # Grab MATLAB plotting functions
from control.matlab import *    # MATLAB-like function
import matplotlib.pyplot as plt

# System parameters
m = 4                          # mass of aircraft
J = 0.0475                     # inertia around pitch axis
r = 0.25                       # distance to center of force
g = 9.8                        # gravitational constant
c = 0.05                       # damping factor (estimated)

# Transfer functions for dynamics
Pi = tf([r], [J, 0, 0])        # inner loop (roll)
Po = tf([1], [m, c, 0])        # outer loop (position)

k = 200
a = 2
b = 50
Ci = k*tf([1, a], [1, b])              # lead compensator
Li = Pi*Ci

Hi = parallel(feedback(Ci, Pi), -m*g*feedback(Ci*Pi, 1)) 

# Now design the lateral control system
a = 0.02  
b = 5  
K = 2 
Co = -K*tf([1, 0.3], [1, 10])          # another lead compensator
Lo = -m*g*Po*Co 

L = Co*Hi*Po 
S = feedback(1, L)
T = feedback(L, 1)

figure(0)
plt.plot(bode(L))
plt.draw()

nyquist(L, (0.0001, 1000))
axis([-700, 5300, -3000, 3000])

figure(1)
plt.plot(nyquist(L, (0.0001, 1000)))
plt.draw()

gangof4(Hi*Po, Co)
figure(2)
plt.plot(gangof4(Hi*Po, Co))
plt.draw()

plt.show()
