import turtle

def draw_diamond(turtle_obj):
    lado = 80
    minor_angle = 30
    major_angle = 150
    turtle_obj.forward(lado)
    turtle_obj.right(minor_angle)
    turtle_obj.forward(lado)
    turtle_obj.right(major_angle)
    turtle_obj.forward(lado)
    turtle_obj.right(minor_angle)
    turtle_obj.forward(lado)
    turtle_obj.right(180)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(100)
    brad.right(90)

    count = 0
    while count < 45:
        draw_diamond(brad)
        brad.right(2)
        count += 1

    brad.forward(300)

    window.exitonclick()


draw_shape()
