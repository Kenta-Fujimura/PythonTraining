import random
import turtle
ts=[]

def setup():
	global ts
	startline=-620
	screen=turtle.Screen()
	screen.setup(1290,720)
	screen.bgpic('pavement.gif')

	t_y=[-60,-40,-20,0,20,40,60,80]
	t_color=['white','black','red','blue','yellow','green','orange','pink']

	for i in range(len(t_y)):
		t=turtle.Turtle()
		t.shape('turtle')
		t.penup()
		t.setpos(startline,t_y[i])
		t.color(t_color[i])
		t.pendown()
		ts.append(t)




def race():
	global ts
	finishline=540

	while True:
		for current_t in ts:
			move=random.randint(0,10)
			current_t.forward(move)

			x=current_t.xcor()
			if x >=finishline:
				winner_color=current_t.color()
				current_t.write('Win!'+winner_color[0],font=('Arial',16,'normal'))
				break
		else:
			continue
		break
		
setup()
race()
turtle.mainloop()
