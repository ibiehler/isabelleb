'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion.
 Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('light pink')


# Problem 1
def recursive_htree(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.back(height / 2)
        my_turtle.right(180)
        my_turtle.forward(height / 2)
        my_turtle.left(180)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.right(90)
        my_turtle.forward(height / 2)
        my_turtle.left(180)
        my_turtle.forward(height)
        recursive_htree(x + height / 2, y + height / 2, height / 2, depth - 1)
        recursive_htree(x + height / 2, y - height / 2, height / 2, depth - 1)
        recursive_htree(x - height / 2, y + height / 2, height / 2, depth - 1)
        recursive_htree(x - height / 2, y - height / 2, height / 2, depth - 1)


recursive_htree(0, 0, 315, 4)

# Problem 2
my_screen.clear()
my_screen.bgcolor('lavender')
my_turtle.color('black')


def plus_fractal(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.back(2 * height)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.back(height * 2)
        plus_fractal(x + height, y, height / 2, depth - 1)
        plus_fractal(x - height, y, height / 2, depth - 1)
        plus_fractal(x, y + height, height / 2, depth - 1)
        plus_fractal(x, y - height, height / 2, depth - 1)


plus_fractal(0, 0, 150, 4)


# Problem 3

my_screen.clear()
my_screen.bgcolor('light blue')
my_turtle.color('black')


def fun_fractal(height, depth):
    my_turtle.goto(0, 0)
    if depth > 0:
        my_turtle.left(12)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        fun_fractal(height - 2, depth - 1)


fun_fractal(360, 180)

my_screen.exitonclick()

