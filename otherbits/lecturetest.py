from graphix import Window, Text, Point
import random
def hello_graphix():
    win = Window("My first window",400,700)
    text = "Hello"
    p = Point(100,500)
    message = Text(p,text)
    message.draw(win)
    while True:
        message.move(0,-10)
        win.get_mouse()
        

hello_graphix()