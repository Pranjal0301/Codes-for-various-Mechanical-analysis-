#Name:Pranjal Pramod Sarode.
#Roll.no:9  Div:D

import numpy as np
import math
print("Please choose the type of material of the rod")
print("For ductile material press 1")
print("For brittle material press 2")
z = int(input())
if(z==1):
              #inputs
    print("Yield strength or σyt : (MPa)")
    ys = float(input())
    print("Axial Tensile Force : (kN)")
    P = float(input())
    print("Torque acting on the rod: (Nm)")
    T = int(input())

    sigma = (2*P*10**3)/math.pi            #value of the sigma

    tau = (16*T)/math.pi                   #value of the tau

    tauMax = ys*10**6/2                    #value of tau max

    #solving with Maximum shear stress theory
    k = np.roots([-((tauMax) ** 2), 0, 0, 0, ((sigma) ** 2),0, (tau ** 2)])           #polynomial eqaution for the diameter
    q = k.real

    if q[0]>0:
        print("The diameter of the rod by Maximum shear stress theory :",q[0]*10**3,"mm")
    else:
        print("The diameter of the rod by Maximum shear stress theory :",q[1]*10**3,"mm")

    #solving with von-Mises criteria(Maximun distorion theory)
    l = np.roots([-((2*tauMax) ** 2), 0, 0, 0, 4*((sigma) ** 2),0, 3*(tau ** 2)])          #polynomial eqaution for the diameter
    e = l.real

    if e[0]>0:
        print("The diameter of the rod by von-Mises criteria :",e[0]*10**3,"mm")
    else:
        print("The diameter of the rod by von-Mises criteria :",e[1]*10**3,"mm")

else:
    print("Ultimate tensile strength sigma ut : (MPa)")
    ut = float(input())
    print("Ultimate compressive strength sigma uc: (MPa)")
    uc = float(input())
    print("Torque acting on the rod :(Nm)")
    T2 = float(input())
    print("Axial Tensile Force acting on the rod :(kN)")
    P2 = float(input())

    x = (1 / (ut * 10 ** 6)) - (1 / (uc * 10 ** 6))

    y = (1 / (ut * 10 ** 6)) + (1 / (uc * 10 ** 6))

    sigma2 = ((4 * P2 * 10 ** 3) / math.pi)        #value of sigma
    tau2 = ((16 * T2) / math.pi)                   #value of tau

    # solving by using Maximum principle stress theory.
    root1 = np.roots([((ut * 10 ** 6) ** 2), 0, -(sigma2 * (ut * 10 ** 6)), 0, 0, 0, -(tau2) ** 2])  #polynomial eqaution for the diameter
    n = root1.real
    if n[0] > 0:
        print("The diameter of the rod by Maximum principle stress theory. :",n[0]*10**3,"mm")
    else:
        print("The diameter of the rod by Maximum principle stress theory. :",n[1]*10**3,"mm")

    # solving by using Mohr's criteria.
    root2 = np.roots([-1, 0, x * sigma2, 0, (y ** 2 - x ** 2) * (sigma2 / 2) ** 2, 0, (tau2 ** 2) * y ** 2])  #polynomial eqaution for the diameter

    m = root2.real
    if m[0] > 0:
        print("The diameter of the rod by Mohr's criteria.:",m[0]*10**3,"mm")
    else:
        print("The diameter of the rod by Mohr's criteria.:",m[1]*10**3,"mm")