from display import *

def slope(x0, y0, x1, y1):
	if (x0-x1 == 0):
		print "Boo! Divison by 0"
		return False

	else:
		rise = float(y1) - float(y0)
		run = float(x1) - float(x0)
		slp = rise / run
		#Oct 1/5
		if ((slp > 0) and (slp <= 1)):
			return 1

		#Oct 2/6
		elif slp > 1:
			return 2

		#Oct 3/7
		elif slp < -1:
			return 3
		#Oct 4/8
		elif ((slp >= -1) and (slp < 0)):
			return 4

		else:
			print "end"
			return False



def draw_line( x0, y0, x1, y1, screen, color ):

	x = x0
	y = y0
	A = y1-y0
	B = -(x1-x0)
	m = slope (x, y, x1, y1)


	#Special Vert / Hor

	if (B == 0):
		while (y <= y1):
			plot(screen,color,x,y)
			y+=1
	elif (A == 0):
		while (x <= y1):
			plot(screen,color,x,y)
			x+=1

	#Oct 1

	elif (m == 1):

		d = 2 * A + B
		while (x <= x1):
			plot(screen,color,x,y)

			if (d > 0):
				y+=1
				d+= 2*B
			x+=1
			d+=2*A

	#Oct 2

	elif (m == 2):
		d = 2 * B + A
		while (y<=y1):
			plot(screen,color,x,y)

			if (d < 0):
				x+=1
				d+= 2*A
			y+=1
			d+=2*B		

	#Oct 8

	elif (m == 4):
		d = 2 * A - B
		while (x<=x1):
			plot(screen,color,x,y)

			if (d < 0):
				y-=1
				d-= 2*B
			x+=1
			d+=2*A	
	#Oct 7

	elif (m == 3):
		d = A-(2*B)
		while (y>=y1):
			plot(screen,color,x,y)

			if (d > 0):
				x+=1
				d+= 2*A
			y-=1
			d-=2*B	
	else: 
		print "something is wrong"

'''
#Test Slopes
print slope (0,0,-1,-10)
print slope (0,0,1,-10)
print slope (0,0,1,1)
print slope (0,0,-2,4)

'''