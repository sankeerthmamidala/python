from turtle import *
pen1 = Pen()
pen2 = Pen()
pen1.screen.bgcolor('#c73e32')
pen1.begin_fill()
for i in range(3):
    pen1.forward(150)
    pen1.left(120)
pen1.end_fill()
