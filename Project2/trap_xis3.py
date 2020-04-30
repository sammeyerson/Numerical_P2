import math
import pandas as pd 

def func(x): return (math.exp(3*x))
    
def deq( x, y ): return (3*y) 
	

def euler( x0, y, h, x ): 

	maxerr=0

	while x0 < x:  
		y = (y+.5*h*deq(x0,y))/(1-1.5*h) 
		x0 = x0 + h
		yact = func(x0)
		err=abs((yact-y)/y)*100
		if err>maxerr:
		    maxerr=err

	print("Approximate solution at x = ", x, " is ", "%.6f"% y,"\n","Error: ", maxerr, "%"," .actual y is::",yact,"\n") 

x0 = 0
y0 = 1
x = 3

h = 0.1
euler(x0, y0, h, x) 


h = 0.01
euler(x0, y0, h, x) 

h = 0.001
euler(x0, y0, h, x) 