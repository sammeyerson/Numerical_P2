import math
import pandas as pd 

def realfunc(x): return (math.exp(3*x))

    
def euler( x0, y, h, x ): 
	maxerror=0
	while x0 < x: 
		y = y + h * (3*y)
		x0 = x0 + h
		yact = realfunc(x0)
		error=abs((yact-y)/y)*100
		if error>maxerror:
		    maxerror=error
	print("Calculated solution at the x: ", x, ": ", "%.6f"% y,"\n","Error: ", maxerror, "%", ". Actual y-value: ",yact, "\n") 


x0 = 0
y0 = 1
x = 3

h = 0.1
euler(x0, y0, h, x) 

h=0.01
euler(x0, y0, h, x) 

h=0.001
euler(x0, y0, h, x) 