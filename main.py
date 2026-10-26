import turtle
from patterns import *

# Input
#words = 'rdabdefhilwmwuwnprtvxz'
words = input("Enter text:	").lower()

# turtle screen setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")  # background color
screen.title("Colorful Turtle Typography")

# create turtle object
_t = turtle.Turtle()
_x = -250
_y = 150
_t.speed(6)
_t.pu()
_t.goto(_x, _y)

_t.shape('turtle')
_t.shapesize(0.5, 0.5)

# Colors
colors = [
    "coral",          # Light Reddish Orange
    "lightseagreen",  # Greenish Blue
    "crimson",        # Bright Red
    "gold",           # Yellowish Gold
    "mediumpurple",   # Purple
    "hotpink",        # Pink
    "springgreen",    # Neon Green
    "orangered",      # Orange Red
    "turquoise",      # Light Cyan Blue
    "violet",         # Violet
    "lime",           # Bright Lime Green
    "dodgerblue",     # Blue
    "magenta",        # Magenta
    "tomato",         # Tomato Red
    "mediumspringgreen", # Fresh Green
    "khaki",          # Light Yellowish
    "orchid",         # Soft Purple
    "deepskyblue",    # Bright Sky Blue
    "yellow"          # Yellow
]

for idx, c in enumerate(words):
    # Update current position
    _x, _y = _t.pos()
    
    # Auto Linebreak Check
    if _x > 230:
        _y -= 60
        _x = -250
        _t.goto(_x, _y)
    
    # Handle space or dynamically call character functions
    if c == ' ':
        space(_t, _x, _y, wh=25)
    elif c in globals() and callable(globals()[c]):
        globals()[c](_t, colors[idx % len(colors)], _x, _y)
    else:
        space(_t, _x, _y)

_t.goto(280, -180)

# keep window open
turtle.done()
