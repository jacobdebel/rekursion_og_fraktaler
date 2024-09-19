import turtle

screen = turle.Screen()
screen.setup(400, 400)

pen = turtle.Turtle()


def setup():
    pen.goto(0, -200)
    pen.pendown()


def tegn_trae(laengde, venstre_vinkel, hoejre_vinkel):
    pen.pendow()
    pen.forward(laengde)
