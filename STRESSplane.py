#NAME :PRANJAL SARODE
#DIV :D   ROLL NO :9

from matplotlib import pyplot as plt  # python lib for  plotting graph
import numpy as np  # python lib for using 2d array
import math  # python lib for using mathematical aretmetics

a = np.array([0, 5, 10, 15, 20, 25, 30, 35, 45])  # array with theta varing from 0-45

A0 = 11250  # perpendicular area of the plane

P = 11000  # tensil load

theta = (a * (math.pi / 180))  # theta (a from line 6) convetd into radians

Atheta = A0 / np.cos(theta)  #area at angle theta in oblique plain
F = P * (np.cos(theta))      #normal force
V = P * (np.sin(theta))      #tangential force

sigma = F / Atheta           #normal Stress
tau  = V / Atheta            #Shear stress

plt.figure()                 #code for plotting of Sigma V theta
fig, ax1 = plt.subplots()
ax1.set_ylabel('Sigma')
ax1.set_xlabel('Theta')
plt.plot(a,sigma)

plt.figure(1)               #code for plotting of tau V theta
fig, ax1 = plt.subplots()
ax1.set_ylabel('Tau')
ax1.set_xlabel('Theta')
plt.plot(a,tau)


plt.figure(2)               #code for plotting of Sigma V tau
fig, ax1 = plt.subplots()
ax1.set_ylabel('sigma')
ax1.set_xlabel('Theta')
ax1.plot(a,sigma, color='blue')
ax1.set_ylim(0.4,1)

ax1.grid()

# Second Line on secondary Y axis
ax2 = ax1.twinx()  # join a second axis with the first graph we just made
ax2.set_ylabel('tau')
ax1.set_xlabel('Theta')
ax2.set_ylim(0,0.6)
ax2.plot(a,tau,color='red')
plt.show()