from turtle import *

def rectangle(x,y,w,h=0,s=0):
    h+=w*(h==0)
    goto(x,y)
    if s == 1:
        begin_fill()
    for i in range(4):
        forward((w*((i+1)%2))+(h*((i)%2)))
        left(90)
def draw_grid(n,s):
    h=int(window_height()/20)*20
    w=int(window_width()/20)*20
    color("black");up()
    for i in range(int(n/2)):
        rectangle((i*s*2)-w/2,h/2,s,s*-n,i+1)
    goto(-w/2,h/2)
    for i in range(int(n/2)):
        rectangle(-w/2,((i+1)*-(s*2))+h/2,s*n,s,0)
    end_fill()

speed(-1)

plateau_size=20
carre_size=20

draw_grid(plateau_size,carre_size)
exitonclick()