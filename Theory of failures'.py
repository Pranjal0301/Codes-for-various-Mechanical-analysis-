import math
print("Yield stength in Mpa")
ys = float(input())
print("Tensile stress in kN")
P = float(input())
print("Diameter of the shaft in mm :")
d = float(input())

sigma = P*1000/((math.pi/4)*d*d)
print(sigma)

tau = math.sqrt((ys/2)**2 - (sigma/2)**2)
#print(tau)

T = (tau*(10**6)*(math.pi)*((d*10**-3)**3))/16
#print(T)

#Max distortion theory

tau2 = math.sqrt((ys**2 - sigma**2)/3)
#print(tau2)

T2 = (tau2*(10**6)*(math.pi)*((d*10**-3)**3))/16
#print(T2)


# for brittle materials

tau3 = math.sqrt((ys - (sigma/2))**2 - (sigma/2)**2)
print(tau3)

T3 = (tau3*(10**6)*(math.pi)*((d*10**-3)**3))/16
print(T3)
print("ut =")
ut = int(input())
print("uc =")
uc = int(input())
R = (1-((1/ut) - (1/uc))*(sigma/2))/((1/ut) + (1/uc))
print(R)

tau4 = math.sqrt(R**2 - (sigma/2)**2)
print(tau4)
T4 = (tau4*(10**6)*(math.pi)*((d*10**-3)**3))/16
print(T4)