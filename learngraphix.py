from graphix import Window, Point,Circle,Line
win = Window()

p = Point(100,60)
p.draw(win)
c = Circle(p,25)
c.draw(win)
p.outline_colour = "white"

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

mouth = Circle(Point(100,70),5)
mouth.draw(win)