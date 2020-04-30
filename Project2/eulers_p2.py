import math
import pandas as pd 

def realfunc(x): return (x/(1+x**2))
def deq( x, y ): return (1/(1+x**2)-2*y**2) 

def euler( x0, y, h, x ): 
	maxerror=0
	while x0 < x: 
		y = y + h * deq(x0,y)
        x0 = x0 + h
		yreal = realfunc(x0)
		error=abs((yact-y)/y)*100
		if error>maxerror:
		    maxerror=error
	print("Calculated solution at the x: ", x, ": ", "%.6f"% y,"\n","Error: ", maxerror, "%", ". Actual y-value: ",yreal, "\n") 



x0 = 0
y0 = 0
x = 10

h = 0.1
euler(x0, y0, h, x) 

h=0.01
euler(x0, y0, h, x) 

h=0.001
euler(x0, y0, h, x) 