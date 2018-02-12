from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#Slope = 1
draw_line(250,250,500,500,screen,color)
draw_line(0,500,250,250,screen,color)
draw_line(0,0,250,250,screen,color)
draw_line(250,250,500,300,screen,color)
draw_line(250,250,500,100,screen,color)
draw_line(250,250,500,50,screen,color)
draw_line(250,250,500,1,screen,color)
draw_line(40,500,250,250,screen,color)
draw_line(0,40,250,250,screen,color)
draw_line(0,140,250,250,screen,color)
draw_line(200,300,200,400,screen,color)
draw_line(250,250,250,500,screen,color)
draw_line(0,250,250,500,screen,color)
draw_line(30,450,290,210,screen,color)


display(screen)
save_extension(screen, 'img.png')
