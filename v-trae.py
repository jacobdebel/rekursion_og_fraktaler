# [[file:Rekursion_og_fraktaler.org::*Tegn et træ med computeren][Tegn et træ med computeren:1]]
import turtle
import math
import time

BREDDE = 800
HOEJDE = 400

def tegn_trae(turtle, laengde, vinkel_v, vinkel_h, skalering, dybde):
    # Regnbuens farver
    farver = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    if dybde > 0:
        # I kan ændre farven på træet på den næste linje
        turtle.color("black") 
        # Hvis træet skal skifte farve, så sæt hashtag foran forrige linje og fjern det fra den næste
        # turtle.color(farver[dybde%len(farver)])
        turtle.down()
        turtle.forward(laengde)
        turtle.left(vinkel_v)
        tegn_trae(turtle, laengde*skalering, vinkel_v, vinkel_h, skalering, dybde-1)
        turtle.right(vinkel_v + vinkel_h)
        tegn_trae(turtle, laengde*skalering, vinkel_v, vinkel_h, skalering, dybde-1)
        turtle.left(vinkel_h)
        turtle.up()
        turtle.backward(laengde)
    else:
        return

# Opsætning
skaerm = turtle.Screen()
skaerm.setup(BREDDE, HOEJDE)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
skaerm.tracer(1) #Ændr til et større tal, hvis animationen tager for lang tid
# Opsætning slut

t.left(90)
t.up()
t.goto(0,-200)
t.down()
dybde = 2
skalering = 1.0
laengde = 80
vinkel_venstre = 30
vinkel_hoejre = 30
tegn_trae(t, laengde, vinkel_venstre, vinkel_hoejre, skalering, dybde)
skaerm.mainloop()
# Tegn et træ med computeren:1 ends here
