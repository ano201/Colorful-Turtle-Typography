# drawing pattern
def space(t, x, y, wh=25):
	t.pu()
	t.goto(x+wh, y)

def vl(t, lng=40):
	t.setheading(0)
	t.pd()
	t.rt(90)
	t.fd(lng)
	t.lt(90)
	t.pu()
	
def hl(t, lng=20):
	t.setheading(0)
	t.pd()
	t.fd(lng)
	t.pu()

def hcr(t):
	t.setheading(0)
	t.pd()
	for rng in range(15):
		if rng <= 3 or rng >= 9 :
			t.fd(3)
			t.rt(10)
		else:
			t.fd(1)
			t.rt(14)
	t.pu()

# Drawing Character

def a(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	t.goto(x+10, y)
	t.pd()
	t.goto(x, y-40)
	t.pu()
	t.goto(x+10, y)
	t.pd()
	t.goto(x+20, y-40)
	t.pu()
	t.goto(x+3, y-30)
	t.pd()
	hl(t, 15)
	space(t, x, y)

def b(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.pu()
	t.goto(x,y)
	hcr(t)
	t.goto(x,y-20)
	hcr(t)
	space(t, x, y, 19)

def d(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.pd()
	t.goto(x, y)
	for i in range(29):
		t.rt(6)
		t.fd(2.1)
	space(t, x, y)

def e(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x, y)
	hl(t)
	t.goto(x, y-20)
	hl(t)
	t.goto(x, y-40)
	hl(t)
	space(t, x, y)
	
def f(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x, y)
	hl(t)
	t.goto(x, y-20)
	hl(t)
	space(t, x, y)
	

def h(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x+20, y)
	vl(t)
	t.goto(x, y-20)
	hl(t)
	space(t, x, y)

def i(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	hl(t)
	t.goto(x, y-40)
	hl(t)
	t.goto(x+10, y)
	vl(t)
	space(t, x, y)

def l(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	hl(t)
	space(t, x, y)

def m(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x, y)
	t.pd()
	t.goto(x+10, y-20)
	t.goto(x+20, y)
	vl(t)
	space(t, x, y)

def n(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x,y)
	t.pd()
	t.goto(x+25,y-40)
	t.pu()
	t.goto(x+25, y)
	vl(t)
	space(t, x, y, 30)

def p(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x, y)
	hcr(t)
	space(t, x, y, 19)
	
def r(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.goto(x, y)
	hcr(t)
	t.pd()
	t.goto(x+18, y-40)
	space(t, x, y, 22)

def t(_t, color, x, y):
	_t.setheading(0)
	_t.pencolor(color)
	hl(_t)
	_t.goto(x+10, y)
	vl(_t)
	space(_t, x, y)
	
	
def u(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t, 20)
	t.goto(x+20, y)
	vl(t, 20)
	t.goto(x, y-20)
	t.pd()
	t.rt(90)
	for a in range(30):
		t.fd(1.6)
		t.lt(2)
		if a > 10 and a < 18:
			t.lt(18)
			t.fd(1.19)
	space(t, x, y)
	

def v(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	t.pd()
	t.goto(x+12.5, y-40)
	t.goto(x+25, y)
	space(t, x, y, 30)

def w(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	vl(t)
	t.pd()
	t.goto(x+10, y)
	t.goto(x+20, y-40)
	t.goto(x+20, y)
	space(t, x, y)

def x(t, color, _x, y):
	t.setheading(0)
	t.pencolor(color)
	t.pd()
	t.goto(_x+25, y-40)
	t.pu()
	t.goto(_x+25, y)
	t.pd()
	t.goto(_x, y-40)
	space(t, _x, y, 30)

def z(t, color, x, y):
	t.setheading(0)
	t.pencolor(color)
	hl(t)
	t.pd()
	t.goto(x, y-40)
	hl(t)
	space(t, x, y)
