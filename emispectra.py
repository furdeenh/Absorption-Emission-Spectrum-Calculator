
def Emission_spectra():
    int_lvl = int(input("Enter i energy level :"))
    fin_lvl = int(input("Enter f energy level :"))
    e_change = ((-1*2.178)/(10**18)) * ((1 / (fin_lvl ** 2)) - (1 / (int_lvl ** 2)))
    
    print(round(e_change, 24))
    
    if int_lvl > fin_lvl:
        k = "Energy emitted"
        print(k)
    elif fin_lvl > int_lvl:
        k = "Energy absorbed"
        print(k)
    
    '''
    import turtle
    wn = turtle.Screen()
    line = turtle.Turtle()
    if int_lvl > fin_lvl:
        line.left(90)
        line.forward(-30)
    elif fin_lvl > int_lvl:
        line.right(90)
        line.forward(30)
    '''
    
    import turtle
    wn = turtle.Screen()
    turtle.title("Atomic Absorbtion")
    line = turtle.Turtle()
    line.pensize(5)
    line.color("red")
    style = ('Arial', 14, 'italic')
    turtle.write('Initial Level to Final Level', font=style, align='center')
    if int_lvl > fin_lvl:
        line.right(90)
        line.forward(180)
    elif fin_lvl > int_lvl:
        line.left(90)
        line.forward(180)
    
    
    
    
    '''
    import matplotlib.pyplot as plt 
    import numpy as np
    
    plt.axvline(x=36, color='b', label='axvline - full height')
    
    plt.legend()
    
    x = np.array([1])
    y = np.array([3, 8, 1, 10])    
    plt.show()
    

    plt.axvline(2, label='pyplot vertical line')
    plt.ylabel("Energy difference bewteen levels")
    plt.legend()
    '''
   
   
   
    


                                          
Emission_spectra()







 
