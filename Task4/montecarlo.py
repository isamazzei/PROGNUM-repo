#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 

fun = input("Enter a function f(x)=")
a=float(input("enter limit a:"))
b=float(input("enter limit b:"))
N=1000
x_random = np.random.uniform(a, b, N)
y= eval(fun)
estimate = (b - a) * np.mean(y)
print(f"Monte Carlo Estimate: {estimate:.4f}")


# In[ ]:




