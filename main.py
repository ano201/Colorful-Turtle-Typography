import turtle

# Input

words = input("Enter your text: ").lower()

# turtle screen setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")  # background color
screen.title("Colorful Turtle Typography")

# create turtle object
t = turtle.Turtle()
x = -250
y = 150
t.speed(6)
t.pu()
t.goto(x, y)

t.shape('turtle')
t.shapesize(0.5, 0.5)

# drawing pattern
def space(wh=25):
    t.pu()
    t.goto(x+wh, y)

def line_break():
	t.pu()
	t.goto(x, y-60)
	
def vl():
	t.setheading(0)
	t.pd()
	t.rt(90)
	t.fd(40)
	t.lt(90)
	t.pu()
	
def hl():
	t.setheading(0)
	t.pd()
	t.fd(20)
	t.pu()

def hcr():
	t.setheading(0)
	t.pd()
	for rng in range(30):
		t.fd(1)
		t.rt(6)
	t.pu()

# Drawing Character

def b(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.pu()
	t.goto(x,y)
	hcr()
	t.goto(x,y-20)
	hcr()
	space(14)

def d(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.pd()
	t.goto(x, y)
	for i in range(29):
		t.rt(6)
		t.fd(2.1)
	space()

def e(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.goto(x, y)
	hl()
	t.goto(x, y-20)
	hl()
	t.goto(x, y-40)
	hl()
	space()
	
def f(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.goto(x, y)
	hl()
	t.goto(x, y-20)
	hl()
	space()
	

def h(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.goto(x+20, y)
	vl()
	t.goto(x, y-20)
	hl()
	space()

def i(color):
	t.setheading(0)
	t.pencolor(color)
	hl()
	t.goto(x, y-40)
	hl()
	t.goto(x+10, y)
	vl()
	space()

def l(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	hl()
	space()

def n(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.goto(x,y)
	t.pd()
	t.goto(x+25,y-40)
	t.pu()
	t.goto(x+25, y)
	vl()
	space(30)

def p(color):
	t.setheading(0)
	t.pencolor(color)
	vl()
	t.goto(x, y)
	hcr()
	t.goto(x+14, y)


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

for idx,c in enumerate(words):
	# Update global coordinates from current turtle position
    x, y = t.pos()
    
    # Dynamically call function matching the character
    if c in globals() and callable(globals()[c]):
        globals()[c](colors[idx%len(colors)])
    else:
        space()
    


t.goto(280, -180)

# keep window open
turtle.done()
