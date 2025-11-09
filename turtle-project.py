
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s_width = 900
s_height = 500
t.speed(20)

def draw():
    show_bg()
    draw_speech()
    draw_kelp()
    draw_fish(150, 45, 145, 70, '#32d2ff', '#0c5394', -(s_width/2), -150)
    draw_fish(150, 45, 145, 70, '#ffd966', '#9900ff', (s_width/4), -150)


def show_bg():
    s.setup(width =900, height=500) #900x500 screen
    s.bgcolor('#85f6f6')
    draw_rectangle(0, '#fff2cc', s_width, s_height / 4, -450, -250)
    

def shift(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_fish(r, pos, fin_pos, l, color, fin_color, x, y):
    draw_oval(r, pos, color, x, y)
    draw_fin(l, fin_pos, fin_color, x + (r/1.5), y - (r/4.5))
    if x < 0:
        draw_eye(r/2, -(s_width/3), y+(r/2))
        shift(x + (l*2.5),y + 10)
    elif x >= 0:
        draw_eye(r/2, (s_width/3), y+(r/2))
        shift(x,y + 10)
    t.circle(-10, extent=90)
        

def draw_kelp():
    draw_triangle(50, 180, '#69a84f', -30, -125)
    draw_triangle(50, 180,  '#69a84f', 0, -125)
    draw_triangle(50, 180, '#69a84f', 30, -125)

def draw_speech():
    draw_speech_bubble('#cee2f3', 0, 0)
    
    
    draw_rectangle(180, '#f6f265', 55, 90, -90, 180)
    draw_plus(15, 90, 'black', -70, 130)
    draw_star(70, 0, '#d5a6bd', -40, 145)
    draw_equal_sign(30, 20, 40, 120)
    draw_clam(30, 0, '#b5a7d7', 130, 120)

def draw_rectangle(pos, color, w, h, x, y):
    shift(x, y)
    t.setheading(pos)
    t.color(color)
    t.begin_fill()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.end_fill()

def draw_star(size, pos, color, x, y):
    shift(x,y)
    t.setheading(pos)
    t.color(color)
    t.begin_fill()
    for x in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_clam(size, pos, color, x, y):
    shift(x,y)
    t.setheading(pos)
    t.color(color)
    t.left(45)
    t.begin_fill()
    t.circle(size, 270)
    t.end_fill()

def draw_oval(r, pos, color, x, y):
    shift(x,y)
    t.setheading(-pos) 
    t.color(color)
    t.begin_fill()
    
    for i in range(2):
    # two arcs

        t.circle(r,90)
        t.circle(r/2,90)
        
    t.end_fill()
    # t.seth(0)

def draw_fin(l, fin_pos, fin_color, x, y):
    shift(x,y)
    t.setheading(fin_pos)
    t.color(fin_color)
    t.begin_fill()
    # if x > 0:
    t.right(90)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.end_fill()

def draw_triangle(size, pos, color, x, y):
    shift(x,y)
    t.setheading(pos)
    t.color(color)
    t.begin_fill()
    t.forward(size/4)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120)
    t.end_fill()

def draw_equal_sign(l, h, x, y):
    shift(x,y)
    t.pensize(5)  
    draw_rectangle(0, 'black', l, h, x, y)

    shift(x, y + (h/2))
    t.left(90)
    t.pencolor('#cee2f3')
    t.forward(l)
 
    t.end_fill()

def draw_plus(size, pos, color, x, y):
    shift(x,y)
    t.setheading(pos)
    t.color(color)
    t.begin_fill()
    for x in range(4):
        t.forward(size/2)
        t.right(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_circle(radius, pos, color, x, y):
    shift(x,y)
    t.setheading(pos)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_speech_bubble(color, x, y):
    shift(x,y)
    t.color(color)

    t.begin_fill()
    
    draw_oval(200, 45, color, x - 145, y + 60)
    
    draw_circle(15, 0, color, (x - 130), (y - 30))
    draw_circle(15, 0, color, (x + 110), (y - 30))

    draw_circle(5, 0, color, (x - 140), (y - 45))
    draw_circle(5, 0, color, (x + 150), (y - 45))

    t.end_fill()

def draw_eye(r, x, y):
    
    draw_circle(r/3, 0, 'white', x, y)
    draw_circle(r/6, 0, 'black', x, y/1.1)


if __name__ == '__main__':
    draw()

turtle.done()