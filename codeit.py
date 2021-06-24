#NAME :PRANJAL SARODE
#DIV :D   ROLL NO :9

from matplotlib import pyplot as plt  # python lib for  plotting graph
import numpy as np  # python lib for using 2d array
import math  # python lib for using mathematical aretmetics
print("Given Stress Tensor")
print( )
A = np.array([[120, -55, -75], [-55, 55, 33], [-75, 33, -85]])

print(A)
print( )
print("The values of Stress Invariants on solving their respective derived formulae")
print( )
I1 = A[0][0] + A[1][1] + A[2][2]
print("I1 = ",I1)

I2 = A[0][0]*A[1][1] + A[0][0]*A[2][2] + A[1][1]*A[2][2] - A[1][0]*A[1][0] - A[1][2]*A[1][2] - A[2][0]*A[2][0]
print("I2 = ",I2)
I3 = np.linalg.det(A)
print("I3 = ",I3)
print( )
print("On substituting the value of I1 I2 I3 in equation :")
print("sigma^3 -I1*sigma^2 + I2*sigma - I3 = 0")
print()
print("We get three values of sigma as:")
I =np.roots([1, -I1, I2, -I3])
print("sigma1 = ",I[0])
print("sigma2 = ",I[1])
print("sigma3 = ",I[2])
print()
print("Now choosing the most +ve value from above values of sigma and using below")
print("Equilibrium equations for element aligned with principle direction")
X = np.array([[A[0][0] - I[0], A[0][1], A[0][2]], [A[1][0], A[1][1] - I[0], A[1][2]], [A[2][0], A[2][1], A[2][2] - I[0]]])
print(X)
print()
print("Replacing the last equation with l^2 + m^2 + n^2 = 1")
print("Thereby replacing n with value 1, Hence A = ")
d = np.array([[X[0][0], X[0][1], X[0][2]], [X[1][0], X[1][1], X[1][2]], [0, 0, 1]])
print(d)
print()
b = np.array([[0], [0], [1]])
print("The value of B = ")
print(b)
print()
DC = np.linalg.solve(d, b)
print("On solving the above linear equations AX = B , We get")
print(DC)

len = math.sqrt(DC[0]*DC[0] + DC[1]*DC[1] + 1)
print(len)
print(DC/(len))