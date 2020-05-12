import numpy as np

def add(a, b):
    """adds a to b"""
    tot = a + b
    return tot;
tot = np.add(2,2);
print("the sum is:", tot)

def subtract(a, b):
    """subtracts a from b"""
    sot = a - b
    return sot;
sot = np.subtract(2,2)
print("the difference is", sot)

def multiply(a, b):
    """multiplies a and b"""
    mult = a * b
    return mult;
mult = np.multiply(3,2)
print("the multiplication is", mult)

def divide(a, b):
    """divides a by b"""
    div = a/b
    return div;
div = np.divide(6,2)
print("the division is", div)
