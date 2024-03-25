# -*- coding: utf-8 -*-
"""
Created on Fri May 21 03:36:02 2021

@author: furdeenh
"""
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = x*2

plt.axis('off')

p = plt.plot(x, y)

p + level('xyz')
'''
x =2
y =3
import turtle
wn = turtle.Screen()
line = turtle.Turtle()
if x>y:
    line.left(90)
    line.forward(-30)
elif x<y:
    line.right(90)
    line.forward(30)
        