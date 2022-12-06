import numpy as np


#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

#Inverse orthogonal matrix
omat_inv = np.array([[0,-1], [1,0]])

#Rotation Matrix
def rot(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return  np.array([[c,-s],[s,c]]) 


