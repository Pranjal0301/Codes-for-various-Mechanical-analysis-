import numpy as np
import math

print("ultimate tensile strength sigma ut :(MPa)")
ut = float(input())
print("ultimate compressive strength sigma uc:")
uc = float(input())
print("Torque")
T2 = float(input())
print("Tensile stess")
P2 = float(input())

x = (1/(ut*10**6)) - (1/(uc*10**6))

y = (1/(ut*10**6)) + (1/(uc*10**6))


sigma2 = ((4*P2*10**3)/math.pi)
tau2 = ((16*T2)/math.pi)

#solving by using maximum principle stress theory.
root1 =  np.roots([((ut*10**6) ** 2), 0, -(sigma2*(ut*10**6)), 0,0,0, -(tau2)**2])
n = root1.real
if n[0]>0:
    print(n[0])
else:
    print(n[1])

#solving by using Mohr's criterian.
root2 =  np.roots([-1,0,x*sigma2,0,(y**2-x**2)*(sigma2/2)**2,0,(tau2**2)*y**2])

m = root2.real
if m[0]>0:
    print(m[0])
else:
    print(m[1])