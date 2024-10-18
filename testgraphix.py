from graphix import Window, Text, Point, Circle
import random
def hello_graphix():
    win = Window("My first window",400,700)
    text = "Hello"
    p = Point(100,500)
    c = Circle(p,25)
    c.draw(win)
    for i in range(2):
        c.move(0,-10)
        win.get_mouse()

    c.moveto(500,400)
    

hello_graphix()
input()