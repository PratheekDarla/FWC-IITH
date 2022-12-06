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
L1 = np.array(([0,1]))  # Normal vector for line 1
L2 = np.array(([1,0]))  # Normal vector for line 2
L3 = np.array(([1,1]))  # Normal vector for line 3
Cons1 = np.array(([0,0,1]))
#Cons2 = np.array(([0,1]))

#To find intersection of line 1,2
nor1 = np.block([[L1], [L2]])
nor1_inv = np.linalg.inv(nor1)

cons12 = np.block([Cons1[0],Cons1[1]])
O = nor1_inv@cons12.T
O = O.reshape((2,))
print(O)

#To find intersection of line 1,3
nor2 = np.block([[L1], [L3]])
nor2_inv = np.linalg.inv(nor2)

cons13 = np.block([Cons1[0],Cons1[2]])
A = nor2_inv@cons13.T
A = A.reshape((2,))
print(A)

#To find intersection of line 2,3
nor3 = np.block([[L2], [L3]])
nor3_inv = np.linalg.inv(nor3)

cons23 = np.block([Cons1[1],Cons1[2]])
B = nor3_inv@cons23.T
B = B.reshape((2,))
print(B)

##Angle between y=0,x=0
##cos_ang = L1@L2/(LA.norm(L1)*LA.norm(L2))
##print(np.arccos(cos_ang),np.pi/2)

#Direction vector of line perpendicular line 3, which is OD
m1 = omat@L3  #Normal vector for perpendicular line from O
m_OD = omat@m1
#print(m1)

#Direction vector of line perpendicular to line 1, which is BE
m2 = omat@L1  #Normal vector for perpendicular line from the point B
m_BE = omat@m2
#print(m1,m2)

#To find intersection of line3 and its prependicular from O(OD)
nor4 = np.block([[m1], [L3]])
nor4_inv = np.linalg.inv(nor4)

cons_per1 = m1.T@O.T
cons_alt1 = np.block([[cons_per1],[Cons1[2]]])

D = nor4_inv@cons_alt1
D = D.reshape((2,))
#print(D)

#To find intersection of line 1 and its prependicular from B(BE)
nor5 = np.block([[m2], [L1]])
nor5_inv = np.linalg.inv(nor5)

cons_per2 = m2.T@B.T
cons_alt2 = np.block([[cons_per2],[Cons1[0]]])

E = nor5_inv@cons_alt2
E = E.reshape((2,))
#print(E)

##To find intersection of two altitutes, which is the Orthocenter
nor6 = np.block([[m1], [m2]])
nor6_inv = np.linalg.inv(nor6)

cons_alt3 = np.block([[cons_per1], [cons_per2]])

O_center = nor6_inv@cons_alt3
O_center = O_center.reshape((2,))
print("Orthocenter of triangle:", O_center)

#Direction vectors of lines 1,2,3
m_OA = omat@L1
m_OB = omat@L2
m_AB = omat@L3


#Generating all lines
k1 = -1
k2 = 1.5
x_OA = line_dir_pt(m_OA,A,k1,k2)
x_OB = line_dir_pt(m_OB,B,k1,k2)
x_AB = line_dir_pt(m_AB,B,k1,k2)
x_OD = line_dir_pt(m_OD,O,-1,0.5)
x_BE = line_dir_pt(m_BE,E,-1,0.5)
#x_OA = line_gen(O,A)
#x_OB = line_gen(O,B)
#x_AB = line_gen(A,B)
#x_OD = line_gen(O,D)
#x_BE = line_gen(B,E)

#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:], color='black')#,label='$y=0$')
plt.plot(x_OB[0,:],x_OB[1,:], color='black')#,label='$x=0$')
plt.plot(x_AB[0,:],x_AB[1,:], color='black')#,label='$x+y=0$')

plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$',linestyle="--")#,label='$Diameter$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$',linestyle="--")#,label='$Diameter$')

#Labeling the coordinates
tri_coords = np.vstack((O,A,B,D,O_center)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','A','B', 'D','']
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

