import turtle


def move(a):
    turtle.forward(a)
    turtle.left(90)


def drawSquare(a):
    for i in range(4):
        move(a)


turtle.speed(1)

drawSquare(60)
turtle.goto(150, 150)
drawSquare(120)

# из фукций можно вернуть несколько значений сразу! Но тогда он вернёт КАРТЕЖ значений!!