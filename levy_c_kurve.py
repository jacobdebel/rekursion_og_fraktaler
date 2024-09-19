# [[file:Rekursion_og_fraktaler.org::*Levy C-kurven tegnet vha python][Levy C-kurven tegnet vha python:1]]
import turtle
import math
import time

BREDDE = 800
HOEJDE = 400

def tegn_linje(turtle, punkt_1, punkt_2, farve):
    turtle.color(farve)
    turtle.up()
    turtle.goto(*punkt_1)
    turtle.down()
    turtle.goto(*punkt_2)
    turtle.up()

def afstand(punkt1, punkt2):
    x1, y1 = punkt1
    x2, y2 = punkt2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def levy_c_kurve(turtle, punkt1, punkt2, farve, dybde):

    if dybde > 0:
        laengde = afstand(punkt1, punkt2) / 2**0.5
        x1, y1 = punkt1
        x2, y2 = punkt2
        vinkel_mellem_punkt1_og_punkt2 = math.atan2((y2 - y1), (x2 - x1))
        nyt_punkt = [
	    punkt1[0]
            + laengde * math.cos(math.radians(-45) + vinkel_mellem_punkt1_og_punkt2),
            punkt1[1]
            + laengde * math.sin(math.radians(-45) + vinkel_mellem_punkt1_og_punkt2),
            ]
        levy_c_kurve(turtle, punkt1, nyt_punkt, farve, dybde - 1)
        levy_c_kurve(turtle, nyt_punkt, punkt2, farve, dybde - 1)
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

dybde = 4
p1 = [-100, 100]
p2 = [100, 100]
farve = "black"

levy_c_kurve(t, p1, p2, farve, dybde)
skaerm.mainloop()
# Levy C-kurven tegnet vha python:1 ends here
