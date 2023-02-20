import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("red")
t.pencolor("white")
t.speed(0)

a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    
    a+=2
    b+=1
    if b == 500:
        break

turtle.done()