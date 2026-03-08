#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy.integrate import quad

print("User Function Integrator")

func_str = input("Enter function f(x): ")
a = float(input("Lower limit: "))
b = float(input("Upper limit: "))

def f(x):
    return eval(func_str)

# quad integration
try:
    area, error = quad(f, a, b)
    print("Integral using quad =", area)

except NameError:
    print("Error: Unknown function used.")
except SyntaxError:
    print("Error: Invalid expression.")

# Monte Carlo integration
N = 10000
x_rand = np.random.uniform(a, b, N)
y = f(x_rand)  

mc_area = (b - a) * np.mean(y)
print("Integral using Monte Carlo =", mc_area)


# In[ ]:




