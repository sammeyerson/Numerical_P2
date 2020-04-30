import math
import pandas as pd 


def func(x): return (x/(1+x**2))
   
def deq( x, y ): return (1/(1+x**2)-2*y**2) 
	
	
def trap( x0, y, h, x ): 

	maxerr=0

	while x0 < x: 
		temp = y 
		y =y+0.5*h*(deq(x0,y)+deq(x0+h,y+h*deq(x0,y)))
		x0=x0+h
		yact = func(x0)
		err=abs((yact-y)/y)*100
		if err>maxerr:
		    maxerr=err

	print("Approximate solution at x = ", x, " is ", "%.6f"% y,"\n","Error: ", maxerr, "%","\n") 


x0 = 0
y0 = 0


x = 10

h = 0.1
trap(x0, y0, h, x) 

h = 0.01
trap(x0, y0, h, x) 

h = 0.001
trap(x0, y0, h, x) 