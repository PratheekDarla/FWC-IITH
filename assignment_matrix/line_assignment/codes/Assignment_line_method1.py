
#Code for finding the Orthocenter of the triangle formed by the lines xy=0 and x+y=1 

#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/user/iith/Python_codes/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if


#Input parameters
A = np.array(([1,0],[0,1]))    # For X,Y axis intersection
B = np.array(([0,0]))

C = np.array(([0,1],[1,1]))    # For X axis, x+y=1 intersection
D = np.array(([0,1]))

E = np.array(([1,0],[1,1]))    # For X axis, x+y=1 intersection

e1 = np.array(([1,0]))

n_OA = A[1,:]                 # Normal vector for x=0
n_OB = A[0,:]                 # Normal vector for y=0
n_AB = C[1,:]                 # Normal vector for x+y=1

#Points of intersection of lines xy=0, x+y=1
x = LA.solve(A,B)
print(x)                      # Point of intersection for x=0,y=0

y = LA.solve(C,D)             #Point of intersection for y=0,x+y=1
print(y)

z = LA.solve(E,D)             #Point of intersection for x=0,x+y=1
print(z)


#Direction vector of line perpendicular to x+y=1, which is OD
m1 = omat@n_AB  #Normal vector for perpendicular line from O(0,0)
m_OD = omat@m1
#print(m1)

F = np.array((m1,E[1,:]))    # For perpendicular line, x+y=1 intersection
w = LA.solve(F,D)
#print(w)

G = np.array((m1,E[0,:]))   # For perpendicular line, x=0 intersection
O_centre = LA.solve(G,B)
print(O_centre)

#Direction vectors of lines x=0, y=0, x+y=1
m_OA = omat@n_OA
m_OB = omat@n_OB
m_AB = omat@n_AB


#print(n_OA)
#print(x,x1,x2)

#Generating all lines
k1 = -1
k2 = 1.5
x_OA = line_dir_pt(m_OA,y,k1,k2)
x_OB = line_dir_pt(m_OB,z,k1,k2)

x_AB = line_dir_pt(m_AB,z,k1,k2)
x_OD = line_dir_pt(m_OD,w,k1,k2)

#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:], color='black')#,label='$y=0$')
plt.plot(x_OB[0,:],x_OB[1,:], color='black')#,label='$x=0$')
plt.plot(x_AB[0,:],x_AB[1,:], color='black')#,label='$x+y=0$')

plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$',linestyle="--")#,label='$Diameter$')

#Labeling the coordinates
tri_coords = np.vstack((x,y,z,w)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O(0,0)','A','B', 'D']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='right') # horizontal alignment can be left, right or center

plt.xlabel('$ X $')
plt.ylabel('$ Y $')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('Orthocenter of Triangle')

#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-8.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-8.pdf"))
#else
plt.show()

