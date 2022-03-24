# Charlie CCG 3/24/2022

import turtle

window = turtle.Screen()
window.setup(1000, 1000)
window.title("Lab 3")
window.bgcolor("grey")
toby = turtle.Turtle()
toby.shape("turtle")
toby.pencolor("purple")

for x in range(3):
    toby.forward(200)
    toby.left(120)

window.mainloop()
