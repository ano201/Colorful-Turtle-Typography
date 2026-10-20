# drawing pattern
def space(_t, x, y, wh=25):
	_t.pu()
	_t.goto(x+wh, y)

def line_break(_t):
	x,y = _t.pos()
	_t.pu()
	_t.goto(x, y-60)
	
def vl(_t, lng=40):
	_t.setheading(0)
	_t.pd()
	_t.rt(90)
	_t.fd(lng)
	_t.lt(90)
	_t.pu()
	
def hl(_t, lng=20):
	_t.setheading(0)
	_t.pd()
	_t.fd(lng)
	_t.pu()

def hcr(_t):
	_t.setheading(0)
	_t.pd()
	for rng in range(15):
		if rng <= 3 or rng >= 9 :
			_t.fd(3)
			_t.rt(10)
		else:
			_t.fd(1)
			_t.rt(14)
	_t.pu()

# Drawing Character

def a(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	_t.goto(x+10, y)
	_t.pd()
	_t.goto(x, y-40)
	_t.pu()
	_t.goto(x+10, y)
	_t.pd()
	_t.goto(x+20, y-40)
	_t.pu()
	_t.goto(x+3, y-30)
	_t.pd()
	hl(_t, 15)
	space(_t, x, y)

def b(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.pu()
	_t.goto(x,y)
	hcr(_t)
	_t.goto(x,y-20)
	hcr(_t)
	space(_t, x, y, 19)

def d(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.pd()
	_t.goto(x, y)
	for i in range(29):
		_t.rt(6)
		_t.fd(2.1)
	space(_t, x, y)

def e(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.goto(x, y)
	hl(_t)
	_t.goto(x, y-20)
	hl(_t)
	_t.goto(x, y-40)
	hl(_t)
	space(_t, x, y)
	
def f(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.goto(x, y)
	hl(_t)
	_t.goto(x, y-20)
	hl(_t)
	space(_t, x, y)
	

def h(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.goto(x+20, y)
	vl(_t)
	_t.goto(x, y-20)
	hl(_t)
	space(_t, x, y)

def i(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	hl(_t)
	_t.goto(x, y-40)
	hl(_t)
	_t.goto(x+10, y)
	vl(_t)
	space(_t, x, y)

def l(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	hl(_t)
	space(_t, x, y)

def n(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.goto(x,y)
	_t.pd()
	_t.goto(x+25,y-40)
	_t.pu()
	_t.goto(x+25, y)
	vl(_t)
	space(_t, x, y, 30)

def p(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.goto(x, y)
	hcr(_t)
	space(_t, x, y, 19)
	
def r(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	vl(_t)
	_t.goto(x, y)
	hcr(_t)
	_t.pd()
	_t.goto(x+13, y-40)
	space(_t, x, y, 20)

def t(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	hl(_t)
	_t.goto(x+10, y)
	vl(_t)
	space(_t, x, y)

def v(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	_t.pd()
	_t.goto(x+12.5, y-40)
	_t.goto(x+25, y)
	space(_t, x, y, 30)

def x(_t, color, _x, y):
	_t.setheading(0)
	_t.pencolor(color)
	_t.pd()
	_t.goto(_x+25, y-40)
	_t.pu()
	_t.goto(_x+25, y)
	_t.pd()
	_t.goto(_x, y-40)
	space(_t, _x, y, 30)

def z(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	hl(_t)
	_t.pd()
	_t.goto(x, y-40)
	hl(_t)
	space(_t, x, y)
