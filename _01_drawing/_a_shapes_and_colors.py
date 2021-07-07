import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')


    # This code makes a new Turtle. Pick a new name for the turtle
    too = turtle.Turtle()

    too.shape('turtle')

    # Make your turtle's shape 'turtle', .shape('turtle')

    too.speed(20)
    # Set your turtle's speed using .speed(2)

    # Set your turtle's color using .color('green') and .pencolor('blue')
    too.color('green')
    too.pencolor('blue')


    # Move your turtle forward using .forward(100)

    for i in range(20):

            for i in range(4):
                too.forward(100)
    # TEST    Did your turtle move forward?
    # Move your turtle left or right using .left(90) or .right(90)
                too.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
            too.goto(244, 22)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
            too.color('black', 'yellow')
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
            too.circle(106, 360, 8)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
            too.end_fill()
    # Draw 3 more shapes with different fill colors!
            too.goto(-200, -100)
            for i in range(4):
                too.forward(100)
                too.right(90)

            for i in range(5):
                too.circle(60, 320, 9)
                too.forward(90)
                too.circle(90, 120, 100)
                too.left(2000)
                too.forward(21)


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
