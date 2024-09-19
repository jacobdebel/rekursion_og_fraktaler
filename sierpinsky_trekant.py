# [[file:Rekursion_og_fraktaler.org::*Sierpenskis trekant tegnet vha python][Sierpenskis trekant tegnet vha python:1]]
import turtle

BREDDE = 800
HOEJDE = 400

def midtpunkt(hjoerne_1, hjoerne_2):
    hjoerne_1_x, hjoerne_1_y = hjoerne_1
    hjoerne_2_x, hjoerne_2_y = hjoerne_2
    midtpunkt_x = (hjoerne_1_x + hjoerne_2_x)/ 2
    midtpunkt_y = (hjoerne_1_y + hjoerne_2_y)/ 2
    return (midtpunkt_x, midtpunkt_y)

def tegn_trekant(turtle, hjoerner, farve):
    turtle.fillcolor(farve)
    turtle.begin_fill()
    for i in range(len(hjoerner)+1):
        turtle.goto(*hjoerner[i % len(hjoerner)])
    turtle.end_fill()
    
def sierpinski(turtle, hjoerner, dybde):
    # Regnbuens farver
    farver = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    
    tegn_trekant(turtle, hjoerner,farver[dybde%len(farver)])
    
    if dybde > 0:
        for i in range(len(hjoerner)):
            nye_hjoerner = [hjoerner[i], midtpunkt(hjoerner[i],hjoerner[(i+1)%len(hjoerner)]),midtpunkt(hjoerner[i],hjoerner[i-1])]
            sierpinski(turtle, nye_hjoerner,dybde -1)
    
# Opsætning
skaerm = turtle.Screen()
skaerm.setup(BREDDE, HOEJDE)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.up()
skaerm.tracer(1) #Ændr til et større tal, hvis animationen tager for lang tid
# Opsætning slut

hjoerne_1 = [-150,-100]
hjoerne_2 = [150,-100]
hjoerne_3 = [0, 160]
hjoerner = [hjoerne_1, hjoerne_2, hjoerne_3]

dybde = 2

sierpinski(t, hjoerner, dybde)

skaerm.mainloop()
# Sierpenskis trekant tegnet vha python:1 ends here
