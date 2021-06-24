#NAME :PRANJAL SARODE
#DIV :D   ROLL NO :9
#Gr.No :11910777


import math
print("Please Enter the Spring Index :")
C = float(input())

print("Please Enter the Number of active coils : ")
N = float(input())
print("Please Enter the Normal force on each spring : ")
P = float(input())

print("Please enter the modulus of rigidity :")
G = float(input())

# For the diameter of the wire using Wahls factor.

K = ((4*C - 1)/(4*C - 4)) + (0.615/C)

tau1 = K*(8*P*C)/math.pi
i = 0

#print(K)
#print(tau1)

set1 =[1670, 1570, 1470, 1420, 1370, 1320, 1270, 1250, 1230, 1190, 1130, 1090]  #chart for steel grade 1
set1_dai = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0]

while i < 12 :
    tau = tau1/(set1_dai[i]*set1_dai[i])
    tauD = 0.3*set1[i]
    #print(tau)
    #print(tauD)
    if tau < tauD :
        print("Spring wire diameter is ",set1_dai[i],"mm for patented and cold-drawn steel wires of Grade 1.")
        break ;
    i+=1


set2 =[2010, 1900, 1820, 1720, 1640, 1570, 1510, 1480, 1440, 1390, 1320, 1260]    #chart for steel grade 2
set2_dai = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0]
j = 0
while j < 12 :
    tau = tau1/(set2_dai[j]*set2_dai[j])
    tauD = 0.3*set2[j]
    #print(tau)
    #print(tauD)


    if tau < tauD :
        print("Spring wire diameter is ", set2_dai[j], "mm for patented and cold-drawn steel wires of Grade 2.")
        break ;
    j+=1


set3 =[2390, 2240, 2090, 1990, 1890, 1830, 1750, 1700, 1660, 1600, 1530, 1460] #chart for steel grade 3
set3_dai = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0]
k = 0
while k < 12 :
    tau = tau1/(set3_dai[k]*set3_dai[k])
    tauD = 0.3*set2[k]
    #print(tau)
    #print(tauD)


    if tau < tauD :
        print("Spring wire diameter is ", set2_dai[k], "mm for patented and cold-drawn steel wires of Grade 3.")
        break ;
    k+=1


set4 =[2580, 2400, 2290, 2160, 2050, 1980, 1890, 1840, 1800, 1750, 1670, 1610]  #chart for steel grade 4
set4_dai = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0]
l = 0
while l < 12 :
    tau = tau1/(set4_dai[l]*set4_dai[l])
    tauD = 0.3*set4[l]
    #print(tau)
    #print(tauD)


    if tau < tauD :
        print("Spring wire diameter is ", set4_dai[l], "mm for patented and cold-drawn steel wires of Grade 4.")
        break ;
    l+=1
print()
print()
print("Taking Spring Diameter : 4.5 mm ")

print()
#For mean coil daimeter
D = C*set2_dai[j]
print("Mean coil diameter :" ,D,"mm")

#For spring index
print("Spring index :",D/set2_dai[j])

print("Style of end connection : Square and ground ends")

#For total numer of coils
nt = N + 2
print("Total number of coils :",nt)

#for free length of the coil

roh = (8*P*(D**3)*N)/((G)*(set2_dai[j]**4))
sl = nt*set2_dai[j]
totalaxialgap = nt - 1

freelen = sl + totalaxialgap + roh
print("The free length of the coil is ",freelen,"mm")

#for max defelection

theta = (16*P*(D**2)*N)/(G*(set2_dai[j]**4))

print("Maximum deflection ",theta)

#for stiffness of spring

p = freelen/(nt -1)

stiffness = P/roh
print("Stiffness =",stiffness )