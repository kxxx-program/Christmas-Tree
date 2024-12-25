import turtle
import random

def get_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    return random.choice(colors)

def draw_snowflakes(snow_count):
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.speed(0)
    for _ in range(snow_count):
        turtle.pencolor("white")
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(-200, 300))
        turtle.pendown()
        density = random.randint(8, 12)
        size = random.randint(5, 10)
        for _ in range(density):
            turtle.forward(size)
            turtle.backward(size)
            turtle.right(360 / density)

def write_names(name_count):
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.speed(0)
    for _ in range(name_count):
        turtle.pencolor(get_color())
        turtle.penup()
        turtle.goto(random.randint(-220, 220), random.randint(-300, 340))
        turtle.pendown()
        names = ["Merry", "Christmas"]
        font_size = random.randint(10, 15)
        text = random.choice(names)
        turtle.write(text, align="center", font=("Arial", font_size, "bold"))

def draw_star(size):
    turtle.pensize(3)
    turtle.pencolor("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_tree(depth, length):
    if depth == 0:
        return
    turtle.pensize(depth)
    turtle.pencolor("green")
    turtle.forward(length)
    turtle.left(30)
    draw_tree(depth - 1, length * 0.7)
    turtle.right(30)
    turtle.right(30)
    draw_tree(depth - 1, length * 0.7)
    turtle.left(30)
    turtle.backward(length)

turtle.speed(0)
turtle.bgcolor("black")
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.setheading(90)
draw_tree(10, 100)
turtle.penup()
turtle.goto(0, -150 + 100 * 10 * 0.7)
turtle.pendown()
draw_star(20)
draw_snowflakes(40)
write_names(15)
turtle.penup()
turtle.goto(0, -300)
turtle.pencolor("red")
turtle.write("Merry Christmas!", align="center", font=("Arial", 30, "bold"))
turtle.done()
