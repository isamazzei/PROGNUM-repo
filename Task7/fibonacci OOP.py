#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    def __init__(self, N, M):
        # N = how many Fibonacci numbers to generate
        # M = divisor used for filtering
        self.M = M
        self.N = N

    def fibo(self):
        # Generate first N Fibonacci numbers
        fibonacci = []
        a = 0  # first number
        b = 1  # second number

        while len(fibonacci) < self.N:
            fibonacci.append(a)  # add current number
            c = a + b            # next Fibonacci number
            a = b                # shift values
            b = c

        return fibonacci

    def divide(self):
        # Return only Fibonacci numbers divisible by M
        filtered = []
        for i in self.fibo():
            if i % self.M == 0:
                filtered.append(i)

        return filtered

# Example 
example = Fibonacci(100, 7)
print(example.fibo())    # prints first 100 Fibonacci numbers
print(example.divide())  # prints those divisible by 7

