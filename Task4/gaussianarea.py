#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2)) + z0
    
# user input
A = float(input("Enter A: "))
x0 = float(input("Enter x0: "))
sig = float(input("Enter sigma: "))
z0 = float(input("Enter z0: "))
a = float(input("Enter lower integration limit: "))
b = float(input("Enter upper integration limit: "))

# compute area
area, error = quad(gauss, a, b, args=(A, x0, sig, z0))
print("Area =", area)

# plot
x = np.linspace(x0-5*sig, x0+5*sig, 200)
y = gauss(x, A, x0, sig, z0)
plt.plot(x, y, label="Gaussian")

# shaded area
x_fill = np.linspace(a, b, 200)
y_fill = gauss(x_fill, A, x0, sig, z0)
plt.fill_between(x_fill, y_fill, alpha=0.3,label=f"Area = {area:.4f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gaussian Area")
plt.legend()

plt.show()


# In[ ]:




