# Charlie CCG 3/24/2022

import turtle

window = turtle.Screen()
window.setup()
window.title("Lab 4")
toby = turtle.Turtle()
toby.speed(3)
toby.color("purple")
toby.fillcolor("blue")

toby.stamp()
toby.speed(10)
toby.penup()
toby.setposition(100,100)
toby.pendown()
toby.goto(200,100)
toby.goto(200,0)
toby.goto(100,0)
toby.goto(100,100)

window.mainloop()
