from turtle import *
from time import sleep

# Funciones para hacer las letras.

# Función para hacer la letra "B"
def b():
    goto(0, 100)  # Posición inicial
    pendown()
    setheading(90)  # Apuntar hacia arriba
    forward(200)  # Línea vertical de la "B"
    right(90)  # Girar a la derecha
    circle(-20, 180)  # Semicircunferencia superior
    goto(0, 100)  # Regresar al borde
    circle(-20, 180)  # Semicircunferencia inferior
    penup()
    goto(30, -50)  # Posición para la siguiente letra

# Función para hacer la letra "P"
def p():
    goto(30, 100)  # Posición inicial
    pendown()
    setheading(90)  # Apuntar hacia arriba
    forward(200)  # Línea vertical de la "P"
    right(90)  # Girar a la derecha
    circle(-20, 180)  # Semicircunferencia
    penup()
    goto(100, -50)  # Posición para la siguiente letra

# Función para hacer la letra "V"
def v():
    goto(100, -50)  # Posición inicial
    pendown()
    setheading(90)  # Apuntar hacia arriba
    forward(100)  # Línea izquierda de la "V"
    right(150)  # Girar a la derecha
    forward(100)  # Línea derecha de la "V"
    penup()
    goto(0, 0)  # Regresar al origen

# Propiedades de la ventana y pincel.
setup(640, 480, 0, 0)
title("Iniciales de nombre y apellido")
pensize(3)
speed(4)

# Dibujar letras
penup()
pencolor("blue")
b()
pencolor("red")
p()
pencolor("green")
v()

hideturtle()
exitonclick()