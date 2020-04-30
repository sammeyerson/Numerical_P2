import math
import pandas as pd 


def deq( x, y ): 
	return (3*y) 

def mid( x0, y, h, x ): 
	maxerror=0

	while x0 < x: 
		y = y+h*deq(x0+.5*h, y+.5*h*(3*y)) 
		x0 = x0 + h
		yreal = math.exp(3*x0)
		error=abs((yreal-y)/y)*100
		if error>maxerror:
		    maxerror=error
	print("Approximate solution at x = ", x, " is ", "%.6f"% y,"\n","Error: ", maxerror, "%", ". Actual value: ", yreal,"\n") 


x0 = 0
y0 = 1
x = 3

h = 0.1
mid(x0, y0, h, x) 

h = 0.01
mid(x0, y0, h, x) 

h = 0.001
mid(x0, y0, h, x) 