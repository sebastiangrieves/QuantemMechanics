import math
import numpy as np
import matplotlib.pyplot as plt

def spectral_density(lamb, temp):
    # imput lambda as micrometer
    # temp is in K
    lamb = lamb*pow(10, -6)
    # print(lamb)
    constant_1 = 8*3.14*6.625*pow(10, -34)*3*pow(10, 8)
    constant22 = (6.625*pow(10, -34)*3*pow(10, 8))/(1.38*pow(10, -23))
    e_risin = pow(math.e, constant22/(lamb*temp))
    first_part = constant_1/pow(lamb, 5)
    second_part = 1/(e_risin-1)
    print(first_part*second_part)


# while True:
#    lamb = float(input('Wavelength (lambda): '))
#    temp = float(input('temperature (kelvin): '))
#    spectral_density(lamb, temp)

# this is the code for the graph

x = []
y = []
for line in open('graphing.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(float(lines[0]))
    y.append(float(lines[1]))

plt.title("Temp Vs Spectral Power Density")
plt.xlabel('Temp')
plt.ylabel('Spectral Power Density')
plt.yticks(y)
plt.plot(x, y, marker='o', c='g')

plt.show()
