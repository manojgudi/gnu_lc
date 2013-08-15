#!/usr/bin/python -tt

from scilab import Scilab
a = Scilab()
x = a.rand(3)
y = a.rand(3)
a.plot(x,y)

print "Yes this works"  

