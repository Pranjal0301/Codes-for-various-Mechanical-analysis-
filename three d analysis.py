#NAME :PRANJAL SARODE
#DIV :D   ROLL NO :9
#Gr.No :11910777


import numpy as np  # python lib for using 3d array
import math  # python lib for using mathematical aretmetics
import sympy as sym  #pythn lib for solvin polynomials
sym.init_printing()
print("Given Stress Tensor")
print( )
A = np.array([[120, -55, -75], [-55, 55, 33], [-75, 33, -85]]) #Given Stress tensor written in form of array

print(A)
print( )
print("The values of Stress Invariants on solving their respective derived formulae")
print( )
I1 = A[0][0] + A[1][1] + A[2][2]                              #equation of I1
print("I1 = ",I1)

I2 = A[0][0]*A[1][1] + A[0][0]*A[2][2] + A[1][1]*A[2][2] - A[1][0]*A[1][0] - A[1][2]*A[1][2] - A[2][0]*A[2][0] #equation of I2
print("I2 = ",I2)
I3 = np.linalg.det(A)                                         #equation of I3
print("I3 = ",I3)
print( )
print("On substituting the value of I1 I2 I3 in equation :")
print("sigma^3 -I1*sigma^2 + I2*sigma - I3 = 0")
print()
print("We get three values of sigma as:")
I =np.roots([1, -I1, I2, -I3])                               #taking the roots of the polynomials
print("sigma1 = ",I[0])
print("sigma2 = ",I[1])
print("sigma3 = ",I[2])
print()
                                                             #solving of direction cosine in principle plane1
print("Solving for Direction cosines on Principle plane1 where sigma = ", I[0])
print("By using the equations below")
l1,m1,n1 = sym.symbols('l1,m1,n1')
f = sym.Eq(l1**2+m1**2+n1**2,1)                                #equation 1
print(f)
print("### The above equation is l1^2+m1^2+n1^2 = 1 ###")
g = sym.Eq((A[0][0]-I[0])*l1+(A[0][1])*m1+A[0][2]*n1,0)        #equation 2
print(g)
h = sym.Eq(A[1][0]*l1+(A[1][1]-I[0])*m1+A[1][2]*n1,0)          #equation 3
print(h)
DC1 = sym.solve([f,g,h],(l1,m1,n1))
print("On solving the above three equations we get",DC1[0])
print("Therefore :")
print("l1 = ",DC1[0][0])
print("m1 = ",DC1[0][1])
print("n1 = ",DC1[0][2])
print()
                                                               #solving of direction cosine in principle plane2
print("Solving for Direction cosines on Principle plane2 where sigma = ", I[1])
print("By using the equations below")
l2,m2,n2 = sym.symbols('l2,m2,n2')
f = sym.Eq(l2**2+m2**2+n2**2,1)                              #equation 1
print(f)
print("### The above equation is l2^2+m2^2+n2^2 = 1 ###")
g = sym.Eq((A[0][0]-I[1])*l2+(A[0][1])*m2+A[0][2]*n2,0)      #equation 2
print(g)
h = sym.Eq(A[1][0]*l2+(A[1][1]-I[1])*m2+A[1][2]*n2,0)        #equation 3
print(h)
DC2 = sym.solve([f,g,h],(l2,m2,n2))
print("On solving the above three equations we get",DC2[0])
print("Therefore :")
print("l2 = ",DC2[0][0])
print("m2 = ",DC2[0][1])
print("n2 = ",DC2[0][2])
print()
                                                               #solving of direction cosine in principle plane3
print("Solving for Direction cosines on Principle plane3 where sigma = ", I[2])
print("By using the equations below")
l3,m3,n3 = sym.symbols('l3,m3,n3')                          #equation 1
f = sym.Eq(l3**2+m3**2+n3**2,1)
print(f)
print("### The above equation is l3^2+m3^2+n3^2 = 1 ###")
g = sym.Eq((A[0][0]-I[2])*l3+(A[0][1])*m3+A[0][2]*n3,0)    #equation 2
print(g)
h = sym.Eq(A[1][0]*l3+(A[1][1]-I[1])*m3+A[1][2]*n3,0)      #equation 3
print(h)
DC3 = sym.solve([f,g,h],(l3,m3,n3))
print("On solving the above three equations we get",DC3[0])
print("Therefore :")
print("l3 = ",DC3[0][0])
print("m3 = ",DC3[0][1])
print("n3 = ",DC3[0][2])