#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:08:40 2018
abre un archivo que tiene atomos y lo prepara para tabajar con sus datos
@author: carlos
"""
import numpy as np

vect = np.genfromtxt('tabla1',dtype = 'str')
new = []
vect2 = []
#select just the elements with the condition Li
for item in range(len(vect)):    
    if vect[item][3] == 'Li':
        new.append(vect[item])
#convert the select list in a whole list of numbers
for cosa in range(len(new)):
    a = int(new[cosa][0])
    b = int(new[cosa][1])
    c = int(new[cosa][2])
    vect2.append(a)
    vect2.append(b)
    vect2.append(c)
print(vect2)

print(vect2[5]-vect2[2])