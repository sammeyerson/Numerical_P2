import math
import pandas as pd 


def realfunc(x):return (x/(1+x**2))
    
def deq( x, y ): return (1/(1+x**2)-2*y**2) 
	

def mid( x0, y, h, x ): 
	maxerror=0

	while x0 < x: 

		y = y+h*deq(x0+.5*h, y+.5*h*deq(x0,y)) 
		x0 = x0 + h
		yreal = realfunc(x0)

		error=abs((yreal-y)/y)*100
		if error>maxerror:
		    maxerror=error
	print("Approximate solution at x = ", x, " is ", "%.6f"% y,"\n","Error: ", maxerror, "%", ". Actual value: ", yreal,"\n") 

x0 = 0
y0 = 0
x = 10

h = 0.1
mid(x0, y0, h, x) 

h = 0.01
mid(x0, y0, h, x) 

h = 0.001
mid(x0, y0, h, x) 