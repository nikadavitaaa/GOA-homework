from turtle import *

def draw_a_square(x, y):
    penup()
    goto(x, y)
    pendown()
    
    for num in range(4):
        forward(100)
        left(90)

draw_a_square(50, 50)



exitonclick()