from turtle import *
import random
pensize(10)
rgb = 'green'
End = 0
block = 1
while True :
 Turtle.pencolor(rgb)
 End = End + 1
 forward(10)
 if End == 100 :
  right(270)
  forward(100)
 block = random.randint(1,3)
    if block  == 1 :
  Turtle.pencolor(red)
 if block == 2 :
  Turtle.pencolor(blue)
 if block == 3 :
  Turtle.pencolor(green)
exitonclick()