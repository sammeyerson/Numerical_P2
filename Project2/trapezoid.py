import math
import pandas as pd 

def func(x): return 2*x/(1+x**2)
a=0
b=6

for i in range(1,4):
    n = 6*10**(i)
    h =(b-a)/n
    t=0.5*(func(a) +func(b))
    for i in range(1,n):
        t=t+func(a+h*i)
    I  = h*t
    
    print(I)