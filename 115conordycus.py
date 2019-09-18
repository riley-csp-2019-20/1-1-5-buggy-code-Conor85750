import turtle as trtl

body = trtl.Turtle()
body.pensize(40)
body.circle(20)

numberlegs = 8
leglong = 90
distance = 369 / numberlegs
body.pensize(5)

loop = 0
while (loop < numberlegs):
  body.goto(0,20)
  body.setheading(distance*loop)
  body.forward(leglong)
  loop = loop + 1

body.penup()
body.goto(-20,-20)
body.pendown()
body.pencolor("red")
body.fillcolor("red")
body.begin_fill()
body.circle(10)
body.end_fill()
body.pencolor("black")
body.circle(5)
body.pencolor("red")
body.fillcolor("red")
body.begin_fill()
body.penup()
body.goto(10,-20)
body.pendown()
body.circle(10)
body.pencolor("black")
body.circle(5)
body.end_fill()

body.hideturtle()

wn = trtl.Screen()
wn.mainloop()