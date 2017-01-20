import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('GTKAgg')
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
    print("The approximate area is", h*s)

trapezoidal(f,10000,0,2)

# using simpson's rule, the added complexity
# in code results in more accurate results
# for about the same amount of processing
def simpsons(func,N,a,b):
    h = 1.0*(b-a)/N
    sum = func(a)+f(b)
    for i in range(1,N,2):
        sum += 4*func(a+i*h)
    for i in range(2,N-1,2):
        sum += 2*func(a+i*h)
    print("The approximate area is",(h/3.0)*sum)

simpsons(f,1000,0,2)
