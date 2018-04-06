import turtle



def draw_trule():
    window= turtle.Screen()
    window.bgcolor("blue")
    flower = turtle.Turtle()
    flower.shape("arrow")
    flower.color("white")
    
    for i in range(1,36):
        flower.forward(140)
        flower.right(30)
        flower.left(90)
        flower.forward(120)
        flower.left(30)
        flower.left(90)

        flower.forward(110)
        flower.right(30)
        flower.left(90)
        flower.forward(110)
        flower.circle(30)
        flower.right(90)

    window.exitonclick()
draw_trule()


