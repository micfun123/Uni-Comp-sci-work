from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def draw_stick_figure():
    win = Window()
    p = Point(100,60)
    p.draw(win)
    c = Circle(p,25)
    c.draw(win)
    p.outline_colour = "white"
    mouth = Circle(Point(100,70),5)
    mouth.draw(win)

    body =Line(Point(100,85),Point(100,150))
    body.draw(win)

    left_leg = Line(Point(100,150),Point(80,200))
    right_leg = Line(Point(100,150),Point(120,200))
    left_leg.draw(win)
    right_leg.draw(win)

    left_arm = Line(Point(100,110),Point(65,100))
    left_arm.draw(win)
    right_arm = Line(Point(100,110),Point(135,100))
    right_arm.draw(win)

    eye_left = Point(90,60)
    eye_right = Point(110,60)
    eye_left.draw(win)
    eye_right.draw(win)


def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)


def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()

def draw_circle():
    win = Window()
    circle_radius = int(input("Enter the radius: "))
    center = Point(200,200)
    c = Circle(center,circle_radius)
    c.draw(win)
    
def draw_archery_target():
    win = Window()
    yellow_radius = 50
    red_radius = yellow_radius * 2
    blue_radius = yellow_radius * 3
    center_point = Point(200,200)
    
    blue_circle = Circle(center_point,blue_radius)
    blue_circle.fill_colour = "blue"
    red_circle = Circle(center_point,red_radius)
    red_circle.fill_colour = "red"
    yellow_circle = Circle(center_point,yellow_radius)
    yellow_circle.fill_colour = "yellow"
    
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)
    

def draw_rectangle():
    win = Window()
    rectangle_height = int(input("Please enter the height: "))
    rectangle_width = int(input("Please enter the width: "))
    top_left_height = 200 - (rectangle_height//2)
    top_left_width = 200 - (rectangle_width//2)
    bottem_left_height = 200 + (rectangle_height//2)
    bottem_left_width = 200 + (rectangle_width//2)
    
    rectangle = Rectangle(Point(top_left_width,top_left_height), Point(bottem_left_width,bottem_left_height))
    rectangle.draw(win)
    
def blue_circle():
    win = Window()
    message = Text(Point(200, 50), "Click from the Center Location: ")
    message.draw(win)
    center_point = win.get_mouse()
    circle = Circle(center_point,100)
    circle.draw(win)
    circle.fill_colour = "blue"
    
def ten_lines():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    for i in range(10):
        p1 = win.get_mouse()
        message.text = "click on second point"
        p2 = win.get_mouse()
        line = Line(p1, p2)
        message.text = "click on first point"
        line.draw(win)
    
def ten_strings():
    win = Window()
    input_box = Entry(Point(200, 100), 10)
    input_box.draw(win)
    message = Text(Point(200, 50), "Enter a string & click on window")
    message.draw(win)
    for i in range(10):
        location = win.get_mouse()
        user_input = input_box.text
        input_text = Text(location,user_input)
        input_text.draw(win)    

def ten_coloured_rectangles():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    for i in range(10):
        p1 = win.get_mouse()
        message.text = "click on second point"
        p2 = win.get_mouse()
        rectangle = Rectangle(p1,p2)
        rectangle.draw(win)
        message.text = "click on first point"




    