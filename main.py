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


def random_color():
    '''returns a random color from a list of colors'''
    return random.choice(pallet)

tim = t
screen = t.Screen()

# configure turtle color graphics
tim.colormode(255) # set color mode to rgb values
tim.pensize(20) # pen size to 20px
tim.setposition(-100, -100) # set start position
x_coordinate = -100
y_coordinate = -100

# def draw_dots():
# extracts 20 colors from an image
color_obj = cg.extract("./Addictive---detail-of-Dam-007.jpg", 20)
pallet = extract_colors(color_obj)