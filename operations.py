import numpy as np

def add(a,b):
    return np.add(a,b)

def subtract(a,b):
    return np.subtract(a,b)

def dot_product(a,b):
    return np.dot(a,b)

def cross_product(a,b):
    return np.cross(a,b)

def magnitude(a):
    return np.linalg.norm(a)