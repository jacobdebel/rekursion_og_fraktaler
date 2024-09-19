# [[file:Rekursion_og_fraktaler.org::*Koch-kurven tegnet vha python][Koch-kurven tegnet vha python:1]]
import turtle
import math
import time

BREDDE = 800
HOEJDE = 400

def afstand(punkt1, punkt2):
    x1, y1 = punkt1
    x2, y2 = punkt2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def tegn_linje(turtle, punkt_1, punkt_2, farve):
    turtle.color(farve)
    turtle.up()
    turtle.goto(*punkt_1)
    turtle.down()
    turtle.goto(*punkt_2)
    turtle.up()
                   
def koch_kurve(turtle, punkt1, punkt2, farve, dybde):
    x1, y1 = punkt1
    x2, y2 = punkt2
    afstand_p1_p2 = afstand(punkt1, punkt2)
    ny_afstand = afstand_p1_p2 / 3
    vinkel_p1_p2 = math.atan2(y2-y1,x2-x1)
    if dybde > 0:
        punkt5 = punkt2
        x2 = x1 + ny_afstand * math.cos(vinkel_p1_p2)
        y2 = y1 + ny_afstand * math.sin(vinkel_p1_p2)
        punkt2 = [x2, y2]
        x3 = x2 + ny_afstand * math.cos(vinkel_p1_p2+math.radians(60))
        y3 = y2 + ny_afstand * math.sin(vinkel_p1_p2+math.radians(60))
        punkt3 = [x3, y3]
        x4 = x3 + ny_afstand * math.cos(vinkel_p1_p2-math.radians(60))
        y4 = y3 + ny_afstand * math.sin(vinkel_p1_p2-math.radians(60))
        punkt4 = [x4, y4]
        koch_kurve(turtle, punkt1, punkt2, farve, dybde -1)
        koch_kurve(turtle, punkt2, punkt3, farve, dybde -1)
        koch_kurve(turtle, punkt3, punkt4, farve, dybde -1)
        koch_kurve(turtle, punkt4, punkt5, farve, dybde -1)
    else:
        tegn_linje(turtle, punkt1, punkt2, farve)
    
# Opsætning
skaerm = turtle.Screen()
skaerm.setup(BREDDE, HOEJDE)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
skaerm.tracer(1) #Ændr til et større tal, hvis animationen tager for lang tid
# Opsætning slut

dybde = 2
p1 = [-200,-100]
p2 = [200,-100]
farve = "black"

koch_kurve(t, p1, p2, farve, dybde)
skaerm.mainloop()
# Koch-kurven tegnet vha python:1 ends here
