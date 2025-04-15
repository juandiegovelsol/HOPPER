from turtle import * 
from time import sleep

# Funciones para hacer las letras.

# Función para hacer la letra "B"
def b2(a, b):
    goto(a, b + 200)
    circle(20, -180)
    goto(a + 100, b + 200)
    circle(20, -180)
    goto(a + 100, b + 100)
    circle(20, -180)
    goto(a + 100, b + 75)
    circle(20, -180)
    goto(a, a)

# Función para hacer la letra "P"
def p2(a, b):
    goto(a, b + 200)
    circle(20, -180)
    goto(a + 100, b + 200)
    circle(20, -180)
    goto(a + 100, b + 100)
    penup()
    goto(a, b)
    pendown()
    goto(a, b + 200)

# Función para hacer la letra "V"
def v2(a, b):
    goto(a, b)
    setheading(90)
    forward(200)
    left(120)
    forward(100)
    left(120)
    forward(100)
    setheading(90)
    backward(200)

# Propiedades de la ventana y pincel.
setup(640, 480, 0, 0)
title("Iniciales de nombre y apellido")
pensize(3)
speed(4)

# Dibujar y mover la letra "B"
i = 1
a = 0
b = 0
x = -50
y = -50
while i <= 3:
    if i == 3:
        pencolor("blue")
        b2(a, b)
        penup()
        goto(x, y)
        pendown()
        i += 1
    else:
        pencolor("blue")
        b2(a, b)
        pencolor("white")
        b2(a, b)
        penup()
        goto(x, y)
        pendown()
        a -= 50
        b -= 50
        x -= 50
        y -= 50
        i += 1

# Reacomodación para escribir la nueva letra "P"
penup()
goto(150, 0)
pendown()

# Dibujar y mover la letra "P"
i = 1
a = 150
b = 0
x = 100
y = -50
while i <= 3:
    if i == 3:
        pencolor("red")
        p2(a, b)
        penup()
        goto(x, y)
        pendown()
        i += 1
    else:
        pencolor("red")
        p2(a, b)
        pencolor("white")
        p2(a, b)
        penup()
        goto(x, y)
        pendown()
        a -= 50
        b -= 50
        x -= 50
        y -= 50
        i += 1

# Reacomodación para escribir la nueva letra "V"
penup()
goto(300, 100)
pendown()

# Dibujar la letra "V"
pencolor("green")
v2(300, 100)

hideturtle()
exitonclick()