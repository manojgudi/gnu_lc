#!/usr/bin/python -tt
from scilab import Scilab
from matplotlib.pyplot import * # Grab MATLAB plotting functions
from control.matlab import *    # MATLAB-like function
import matplotlib.pyplot as plt
import sciscipy

sci = Scilab()
sciscipy.eval("s=%s;h=syslin('c',s+1,s^2+s+1);t=0:0.01:10;r=tf2ss(h),a=csim('step',t,r),f=scf(0),plot2d(t,a), xs2bmp(0, 'plot.bmp')")
print "I am awesome"
b = sciscipy.read("a")
t = sciscipy.read("t")

plt.plot(t,b)
plt.show()
