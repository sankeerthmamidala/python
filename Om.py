from turtle import *
pen1 = Pen()
pen2 = Pen()
pen3 = Pen()
pen1.color('#e07e33')
pen2.color('#e07e33')
pen3.color('#e07e33')
for i in range(0,250):
    pen1.forward(1)
    pen1.left(1)
for j in range(0,280):
    pen2.forward(1.5)
    pen2.right(1)
pen3.up()
pen3.goto(150,-30)
pen3.down()
pen3.forward(100)
for i in range(0,270):
    pen3.backward(0.99)
    pen3.right(1)
