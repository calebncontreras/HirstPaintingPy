import colorgram as cg
import turtle as t
import random


def extract_colors(obj):
    """Takes a color obj as argument extracts and returns a tuple og rgb values."""
    color_pallet = []

    for color in obj:
        color_ = color.rgb
        color_pallet.append((color_.r, color_.g, color_.b))

    return color_pallet


def draw_row(row_length):
    """draws a row of row_length and randomly colored dots each dot 50 pixels apart"""
    for _ in range(row_length):
        t.pencolor(random_color())
        t.pendown()
        t.forward(1)
        t.penup()
        t.forward(50)


def random_color():
    """returns a random color from a list of colors"""
    return random.choice(pallet)


tim = t
screen = t.Screen()

# def draw_dots():
# extracts 20 colors from an image
color_obj = cg.extract("./Addictive---detail-of-Dam-007.jpg", 20)
pallet = extract_colors(color_obj)

# configure turtle color graphics
tim.colormode(255)  # set color mode to rgb values
tim.pensize(20)  # pen size to 20px
tim.setposition(-100, -100)  # set start position
x_coordinate = -100
y_coordinate = -100

# stop drawing as turtle moves back to beginning of row
tim.penup()
for _ in range(10):
    draw_row(10)  # set number of dots in each row
    y_coordinate += 50  # move row up by 50px after finished with a row
    tim.setposition(-100, y_coordinate)  # reset row to new left of screen

print(pallet)
screen.exitonclick()
