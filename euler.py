import numpy as np

# integrating functions...
# lets take for example: f(x) = x^4-2x+1
# and integrate from x=0 to x=2 using the 
# trapezoidal rule

def f(x):
    return x**4 - 2*x + 1
def trapezoidal(func,N,a,b):
    s = 0.5*(func(a) + func(b))
    
    h = (b-a)*(1.0)/N
    
    for i in range(1,N):
        s += func(a + i*h)
    print "The approximate area is", h*s " using ", N

trapezoidal(f,10,0,2)

