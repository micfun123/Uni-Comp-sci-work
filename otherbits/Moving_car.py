from graphix import Window, Point, Circle, Line, Rectangle, Polygon
import time

def moving_car():
    win = Window("",700,400)
    
    roof_point_top = Point(100,100)
    roof_point_bottom = Point(250,150)
    roof = Rectangle(roof_point_top,roof_point_bottom)
    roof.fill_colour = "light blue"

    windscreenlist = [Point(250,100),Point(300,150),Point(300,200),Point(250,150)]
    windscreen = Polygon(windscreenlist)
    windscreen.fill_colour = "light blue"

    body_top = Point(50,150)
    body_bottom = Point(300,200)
    body = Rectangle(body_top,body_bottom)
    body.fill_colour = "blue"

    wheel1 = Circle(Point(100,200),25)
    wheel1.fill_colour = "black"
    wheel2 = Circle(Point(250,200),25)
    wheel2.fill_colour = "black"

    roof.draw(win)
    windscreen.draw(win)
    body.draw(win)
    wheel1.draw(win)
    wheel2.draw(win)

    #make it move
    for i in range(1000):
        body.move(5,0)
        wheel1.move(5,0)
        wheel2.move(5,0)
        windscreen.move(5,0)
        roof.move(5,0)
        win.update()
        time.sleep(0.1)

moving_car()