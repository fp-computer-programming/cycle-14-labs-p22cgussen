# Charlie CCG 3/24/2022

import turtle

window = turtle.Screen()
toby = turtle.Turtle()
toby.color(window.textinput("Color", "Enter a color?"))
size = int(window.textinput("Size", "Enter the size of the turtle(1-5)?"))
if size > 5:
    toby.shapesize(5)
elif size < 1:
    toby.shapesize(1)
else:
    toby.shapesize(size)

toby.begin_fill()
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.end_fill()

window.listen()
window.mainloop()
