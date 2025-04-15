from turtle import *

# Funciones mejoradas para hacer las letras.

# Función para hacer la letra "B"
def draw_b():
    penup()
    goto(-150, 0)
    pendown()
    setheading(90)
    forward(200)
    right(90)
    circle(-50, 180)
    left(180)
    circle(-50, 180)

# Función para hacer la letra "P"
def draw_p():
    penup()
    goto(-50, 0)
    pendown()
    setheading(90)
    forward(200)
    right(90)
    circle(-50, 180)
    end_fill()

# Función para hacer la letra "V"
def draw_v():
    penup()
    goto(100, 200)
    pendown()
    setheading(-60)
    forward(115)
    left(120)
    forward(115)

# Configuración de la ventana y el pincel.
setup(640, 480)
title("PVB Logo")
pensize(5)
speed(3)

# Dibujar las letras
pencolor("red")
draw_p()
pencolor("green")
draw_v()
pencolor("blue")
draw_b()

hideturtle()
exitonclick()