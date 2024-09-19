# [[file:Rekursion_og_fraktaler.org::*HTX][HTX:1]]
import turtle

BREDDE = 800
HOEJDE = 600

def tegn_linje(turtle, punkt_1, punkt_2, farve):
    turtle.color(farve)
    turtle.up()
    turtle.goto(*punkt_1)
    turtle.down()
    turtle.goto(*punkt_2)
    turtle.up()

def tegn_H(turtle, centrum, bredde, hoejde,skalering, dybde):
    x,y = centrum
    oppe_venstre = [x- bredde/2, y+hoejde/2]
    nede_venstre = [x-bredde/2,y-hoejde/2]
    oppe_hoejre = [x+ bredde/2, y+hoejde/2]
    nede_hoejre = [x+bredde/2,y-hoejde/2]
    
    tegn_linje(turtle,[x-bredde/2,y],[x+bredde/2, y],farver[dybde%len(farver)])
    tegn_linje(turtle, oppe_venstre, nede_venstre,farver[dybde%len(farver)])
    tegn_linje(turtle, oppe_hoejre, nede_hoejre,farver[dybde%len(farver)])
    turtle.goto(centrum)

    if dybde > 0:
        for hjoerne in [oppe_venstre, nede_venstre, oppe_hoejre, nede_hoejre]:
            tegn_H(turtle, hjoerne, bredde*skalering, hoejde*skalering,skalering, dybde-1)

def tegn_T(turtle, centrum, bredde, hoejde, skalering, dybde):
    x,y = centrum
    oppe_venstre = [x- bredde/2, y+hoejde/2]
    oppe_hoejre = [x+ bredde/2, y+hoejde/2]
    nede_midt_for= [x,y-hoejde/2]
    oppe_midt_for = [x, y+hoejde/2]
    tegn_linje(turtle,nede_midt_for, oppe_midt_for, farver[dybde%len(farver)])
    tegn_linje(turtle,oppe_venstre, oppe_hoejre, farver[dybde%len(farver)])
    turtle.goto(centrum)

    if dybde > 0:
        for ende in [oppe_venstre, oppe_hoejre, nede_midt_for]:
            tegn_T(turtle, ende, bredde*skalering, hoejde*skalering, skalering, dybde-1)

def tegn_X(turtle, centrum, bredde, hoejde, skalering, dybde):
    x,y = centrum
    oppe_venstre = [x- bredde/2, y+hoejde/2]
    oppe_hoejre = [x+ bredde/2, y+hoejde/2]
    nede_venstre= [x-bredde/2,y-hoejde/2]
    nede_hoejre= [x+bredde/2,y-hoejde/2]
    tegn_linje(turtle,oppe_venstre, nede_hoejre, farver[dybde%len(farver)])
    tegn_linje(turtle,oppe_hoejre, nede_venstre, farver[dybde%len(farver)])
    turtle.goto(centrum)

    if dybde > 0:
        for ende in [oppe_venstre, oppe_hoejre, nede_venstre, nede_hoejre]:
            tegn_X(turtle, ende, bredde*skalering, hoejde*skalering, skalering, dybde-1)

# Opsætning
skaerm = turtle.Screen()
skaerm.setup(BREDDE, HOEJDE)
farver = ["blue","green", "red"]
turtles =[]
for _ in range(3):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    turtles.append(t)
skaerm.tracer(0)
# Opsætning slut

dybde = 0
skalering = 0.5

tegn_H(turtles[0], (-100,0),50,100,skalering,dybde)
tegn_T(turtles[1], (0,0),50,100,skalering,dybde)
tegn_X(turtles[2], (100,0), 50, 100, skalering,dybde)

skaerm.update()
skaerm.mainloop()
# HTX:1 ends here
