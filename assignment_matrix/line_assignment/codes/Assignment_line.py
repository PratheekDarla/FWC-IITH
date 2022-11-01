#Code for finding the Orthocenter of the triangle formed by the lines xy=0 and x+y=1 

#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/iith_Prath/Python_codes/CoordGeo') #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if


#Input parameters
L1 = np.array(([0,1]))  # Normal vector for y=0
L2 = np.array(([1,0]))  # Normal vector for x=0
L3 = np.array(([1,1]))  # Normal vector for x+y=1
Cons1 = np.array([[0,1]])
Cons2 = np.array([[0,0]])

print([Cons1[0,1]])
#To find intersection of x=0, y=0
nor1 = np.block([[L1], [L2]])
nor1_inv = np.linalg.inv(nor1)

O = nor1_inv@Cons2.T
O = O.reshape((2,))
print(O)

#To find intersection of y=0, x+y=1
nor2 = np.block([[L1], [L3]])
#print(nor2)
nor2_inv = np.linalg.inv(nor2)

A = nor2_inv@Cons1.T
A = A.reshape((2,))
print(A)

#To find intersection of x=0, x+y=1
nor3 = np.block([[L2], [L3]])
nor3_inv = np.linalg.inv(nor3)

B = nor3_inv@Cons1.T
B = B.reshape((2,))
print(B)

#Angle between y=0,x=0
#cos_ang = L1@L2/(LA.norm(L1)*LA.norm(L2))
#print(np.arccos(cos_ang),np.pi/2)

#Direction vector of line perpendicular to x+y=1, which is OD
m1 = omat@L3  #Normal vector for perpendicular line from O(0,0)
m_OD = omat@m1
#print(m1)

#Direction vector of line perpendicular to y=0, which is BE
m2 = omat@L1  #Normal vector for perpendicular line from the point B
m_BE = omat@m2
#print(m1,m2)

##To find intersection of x+y=1 and its prependicular from O(0,0)
#nor4 = np.block([[m1], [L3]])
#nor4_inv = np.linalg.inv(nor4)
#
#D = nor4_inv@Cons1.T
#D = D.reshape((2,))
##print(D)


#To find intersection of x+y=1 and its prependicular from O(0,0)
nor4 = np.block([[m1], [L3]])
nor4_inv = np.linalg.inv(nor4)

cons_nor1 = m1.T@O.T
#print(cons_nor2, Cons1[0,0])
cons_nor_bl1 = np.block([[cons_nor1],[Cons1[0,1]]])

#print(cons_nor_bl, nor6_inv)
D = nor4_inv@cons_nor_bl1
D = D.reshape((2,))
print(D)

#To find intersection of y=0 and its prependicular from B
nor6 = np.block([[m2], [L1]])
nor6_inv = np.linalg.inv(nor6)

cons_nor2 = m2.T@B.T
#print(cons_nor2, Cons1[0,0])
cons_nor_bl = np.block([[cons_nor2],[Cons1[0,0]]])

#print(cons_nor_bl, nor6_inv)
E = nor6_inv@cons_nor_bl
E = E.reshape((2,))
print(E)

##To find intersection of two altitutes, which is the Orthocenter
nor7 = np.block([[m1], [m2]])
nor7_inv = np.linalg.inv(nor7)

cons_nor3 = m2.T@B.T
#print(cons_nor3, Cons1[0,0])
cons_nor_bl_2 = np.block([[Cons1[0,0]], [cons_nor3]])
print(cons_nor_bl_2)
#print(cons_nor_bl, nor6_inv)
Ortho = nor7_inv@cons_nor_bl_2
Ortho = Ortho.reshape((2,))
print("Orthocenter of triangle:", Ortho)
#To find intersection of two altitudes, which is the Orthocentre
#nor5 = np.block([[m1], [m2]])
#nor5_inv = np.linalg.inv(nor5)
#
#O_centre = nor5_inv@Cons2.T
#O_centre = O_centre.reshape((2,))
#print("Orthocenter of triangle:", O_centre)

#Direction vectors of lines x=0, y=0, x+y=1
m_OA = omat@L1
m_OB = omat@L2
m_AB = omat@L3


#Generating all lines
k1 = -1
k2 = 1.5
x_OA = line_dir_pt(m_OA,A,k1,k2)
x_OB = line_dir_pt(m_OB,B,k1,k2)

x_AB = line_dir_pt(m_AB,B,k1,k2)
#x_OD = line_dir_pt(m_OD,O,k1,k2)
x_OD = line_gen(O,D)
x_BE = line_gen(B,E)


#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:], color='black')#,label='$y=0$')
plt.plot(x_OB[0,:],x_OB[1,:], color='black')#,label='$x=0$')
plt.plot(x_AB[0,:],x_AB[1,:], color='black')#,label='$x+y=0$')

plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$',linestyle="--")#,label='$Diameter$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$',linestyle="--")#,label='$Diameter$')

#Labeling the coordinates
tri_coords = np.vstack((O,A,B,D,E)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O(0,0)','A','B', 'D', 'E']
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
plt.savefig('/sdcard/Download/iith_Prath/Python_codes/Assignment_line.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/iith_Prath/Python_codes/Assignment_line.pdf"))
#else
#plt.show()

