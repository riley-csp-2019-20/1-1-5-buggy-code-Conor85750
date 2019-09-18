import turtle as trtl

body = trtl.Turtle()
body.pensize(40)
body.circle(20)

numberlegs = 8
leglong = 90
distance = 315 / numberlegs
body.pensize(5)

loop = 0
while (loop < numberlegs):
  body.setheading(distance*numberlegs-45)
  body.goto(0,20)
  body.setheading(distance*loop)
  body.forward(leglong)
  body.setheading(distance*numberlegs+45)
  loop = loop + 1

body.hideturtle()

wn = trtl.Screen()
wn.mainloop()