import turtle
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

ja = turtle.Turtle()
ja.speed(5)

rectangle_1 = Rectangle(30,30,60,100)
rectangle_1.setColor("orange")
rectangle_1.draw(ja)

rectangle_2 = Rectangle(-85,85,160,40)
rectangle_2.setColor("black")
rectangle_2.draw(ja)

triangle = Triangle(60,0,100)
triangle.setColor("red")
triangle.draw(ja)

circle = Circle(0,0,40)
circle.setColor("green")
circle.draw(ja)

turtle.exitonclick()