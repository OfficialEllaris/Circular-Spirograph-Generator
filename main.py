import random
import turtle as turtle

turtle.colormode(255)
travis = turtle.Turtle()


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    generated_color = (r, g, b)
    return generated_color


travis.speed("fastest")


def generate_spirograph(shape_gap):
    radii = [100, 80, 60, 40, 20]  # List of radii for the circles
    for _ in range(int(360 / shape_gap)):
        for radius in radii:  # Inner loop to draw circles of different radii
            travis.color(generate_color())
            travis.circle(radius)
        travis.setheading(travis.heading() + shape_gap)


generate_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
