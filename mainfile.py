# -*- coding: utf-8 -*-
"""
@author: Furdeen Hasan
"""
def AbsorbvsEmission_spectra():
    h = 6.63 / (10**34)
    print ("Planck's constant: ", h, "Js")
    c = (3* (10**8))
    print ("Speed of Light:", c, "m/s")
    
    
    
    
    intial_lvl = int(input("Enter initial energy level: "))
    final_lvl = int(input("Enter final energy level: "))
    e_change = ((-1*2.178)/(10**18)) * ((1 / (final_lvl ** 2)) - (1 / (intial_lvl ** 2)))
    wavelength = abs(((h*(c))/ e_change)* (10**9))
    
    
    
    print("Energy change:", round(e_change, 24), "J")
    print("Wavelength of the line in the spectrum:", round(wavelength, 3), "nm")
    
    if intial_lvl > final_lvl:
        k = "Energy emitted by the electron"
        print(k)
    elif final_lvl > intial_lvl:
        k = "Energy absorbed by the electron"
        print(k)
    
    
    import turtle
    wn = turtle.Screen()
    turtle.title("Atomic Absorbtion vs Emission")
    line = turtle.Turtle()
    line.pensize(5)
    line.color("red")
    style = ('Arial', 14, 'italic')
    turtle.write('Energy of the electron', font=style, align='center')
    if intial_lvl > final_lvl:
        line.color("blue")
        line.right(90)
        line.forward(180)
    elif final_lvl > intial_lvl:
        line.left(90)
        line.forward(180)
        
        
AbsorbvsEmission_spectra()        
