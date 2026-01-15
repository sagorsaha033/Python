import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#4a4a4a")
# screen.title("Jumma Mubarak Post")  # Removed to avoid AttributeError
screen.setup(width=800, height=800)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Function to draw a diamond
def draw_diamond(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(45)
    pen.color(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

# Function to draw a star
def draw_star(x, y, size, color):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.penup()
    star.goto(x, y)
    star.setheading(-72)
    star.color(color)
    star.begin_fill()
    star.pendown()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

# Function to type text slowly
def type_slowly(x, y, text, font_size, color="white", delay=0.2, align="center"):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.color(color)

    output = ""
    for char in text:
        output += char
        writer.clear()
        writer.write(output, align=align, font=("Arial", font_size, "bold"))
        time.sleep(delay)

# Draw left and right diamonds
draw_diamond(-120, 0, 30, "#f28c28")
draw_diamond(120, 0, 30, "#f28c28")

# Draw multiple stars
star_positions = [(-200, 200), (-100, 250), (0, 220), (100, 250), (200, 200), (-150, 100), (150, 100)]
for pos in star_positions:
    draw_star(pos[0], pos[1], 40, "#f28c28")

# Slowly type Arabic text
type_slowly(0, 50, "جمعة مباركة", 36, color="white", delay=0.3)

# Slowly type English text
type_slowly(0, -200, "JUMMAH MUBARAK", 24, color="white", delay=0.1)

# Keep the window open
turtle.done()
