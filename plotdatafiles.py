#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:18:30 2018
abre varios archivos para ser graficados,
calcula el promedio de las graficas
hace una regresion lineal del promedio
grafica data y model
@author: carlos
"""

import numpy as np
import matplotlib.pyplot as plt 

#readfiles
x311 = np.genfromtxt('diff313.txt')
x312 = np.genfromtxt('diff314.txt')
x313 = np.genfromtxt('diff317.txt')
x314 = np.genfromtxt('diff318.txt')
x315 = np.genfromtxt('diff319.txt')

#select the points for the linear behavior
y311 = x311[3:18]
y312 = x312[3:18]
y313 = x313[3:18]
y314 = x314[3:18]
y315 = x315[3:18]

#do average of curves
promedio311= []
for i in range(len(y311)):
    suma = y311[i]+ y312[i] + y315[i]+ y313[i]+ y314[i]
    prom= promedio311.append(suma/5)

#do linear regression and evaluate the parameters 
t = np.linspace(1,len(y311),len(y311))

p311 = np.polyfit(t,promedio311,1)
p312 = np.polyval(p311,t)
print (p311)

#plot data
plt.plot(t, promedio311, 'ro', t, p312, 'k')
plt.ylabel('y')
plt.xlabel('x') 
plt.legend(['data','model'])
#plt.title('Stg. 3 Config. 1 negative modifier')
#plt.savefig('Fig1MSD.png') salva la figura
plt.show()


