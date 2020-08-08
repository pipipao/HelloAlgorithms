import turtle

t = turtle.Turtle()
s = turtle.Screen()


def drawSpiral(t, l):
    if l > 0:
        t.forward(l)
        t.right(90)
        drawSpiral(t, l - 5)


def drawTree(t, l):
    if l > 5:
        t.forward(l)
        t.right(20)
        drawTree(t, l - 15)
        t.left(40)
        drawTree(t, l - 10)
        t.right(20)
        t.backward(l)


if __name__ == '__main__':
    # drawSpiral(t, 100)
    drawTree(t, 100)
    s.exitonclick()
