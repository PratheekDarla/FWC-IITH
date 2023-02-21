import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/iith_Prath/Python_codes/CoordGeo') #path to my scri    pts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

import subprocess
import shlex


##Optimization to find 'r' for maximum area
def f(r):
    return ((r*((100-(r**2))**(3/2)))/100)
def df(r):
    return ((100-(r**2))**(3/2) - 3*(r**2)*(100-(r**2))**(1/2))/100

#For maxima using gradient ascent
cur_x = 0.5
alpha = 0.0001 
precision = 0.000000001 
previous_step_size = 1
max_iters = 10000000
iters = 1000

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1 

print('val:',cur_x)
max_val = f(cur_x)

#print(area, max_val)
print("<Maximum area of traingle is", max_val, "at","r =",cur_x)


#Plotting f(x)
x=np.linspace(0,10,100)
y=f(x)
label_str = "$(r/100) (100-r^2)^{3/2}$"
#plt.plot(x,y,label=label_str)
#
##Labelling points
#plt.plot(cur_x,max_val,'o')
#plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')
#
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.grid()
#plt.legend(loc = 'lower center')
#
#plt.savefig('/sdcard/Download/iith_Prath/assignment_matrix/circle_assignment/figs/fig-opt.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/Download/iith_Prath/assignment_matrix/circle_assignment/figs/fig-opt.pdf"))

# Standard basis vectors
e1 = np.array(([1,0])).reshape((2,1))
e2 = np.array(([0,1])).reshape((2,1))

#Input parameters
r = round(cur_x,1)                    # Radius of circle at max area
h = np.array((6,8)).reshape((2,1))    # Given point
o = np.array((0,0)).reshape((2,1))     # Origin

V = np.eye(2)
u = np.zeros((2,1))
f = -r**2
S = (V@h+u)@(V@h+u).T-(h.T@V@h+2*u.T@h+f)*V

##Center and point
center = -u.T

# Intermediate parameters
f0 = np.abs(f+u.T@LA.inv(V)@u)

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(S)
lam1 = D_vec[0]
lam2 = D_vec[1]
p1 = P[:,1].reshape(2,1)
p2 = P[:,0].reshape(2,1)
D = np.diag(D_vec)

t1= np.sqrt(np.abs(D_vec))
negmat = np.block([e1,-e2]).reshape(2,2)
t2 = negmat@t1

#Normal vectors to the conic
n1 = P@t1
n2 = P@t2

#kappa
den1 = n1.T@LA.inv(V)@n1
den2 = n2.T@LA.inv(V)@n2

k1 = np.sqrt(f0/(den1))
k2 = np.sqrt(f0/(den2))

# Possible points of contact  
q11 = LA.inv(V)@((k1*n1-u.T).T)
q12 = LA.inv(V)@((-k1*n1-u.T).T)
q21 = LA.inv(V)@((k2*n2-u.T).T)
q22 = LA.inv(V)@((-k2*n2-u.T).T)

q12 = q12.reshape((2,))
q21 = q21.reshape((2,))

#print(q11,q12,q21,q22)
h1 = np.array((6,8))

#Generating all lines
xhq12 = line_gen(h1,q12)
xhq21 = line_gen(h1,q21)
q12q21 = line_gen(q12,q21)

##Generating the circle
x_circ= circ_gen(center,r)

#Plotting all lines
plt.plot(xhq12[0,:],xhq12[1,:],label='$Tangent1$')
plt.plot(xhq21[0,:],xhq21[1,:],label='$Tangent2$')
plt.plot(q12q21[0,:],q12q21[1,:],label='$Chord$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')

#Labeling the coordinates
tri_coords = np.vstack((h.T,q11.T,q12.T,q21.T,q22.T,center)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['vec{P}_1','C','A','B','D','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='left') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
#if using termux
plt.savefig('/sdcard/Download/iith_Prath/assignment_matrix/circle_assignment/figs/fig-circle1.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/iith_Prath/assignment_matrix/circle_assignment/figs/fig-circle1.pdf"))
