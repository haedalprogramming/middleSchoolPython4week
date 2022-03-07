import turtle as t

gameon = False


def turnright():
    t.setheading(0)


def turnleft():
    t.setheading(180)


def turnup():
    t.setheading(90)


def turndown():
    t.setheading(270)


def runforward():
    global gameon
    t.forward(10)
    if gameon:
        t.ontimer(runforward, 100)


def main():
    global gameon
    t.shape('turtle')
    t.color('white')
    t.up()
    t.onkeypress(turnright, 'Right')
    t.onkeypress(turnleft, 'Left')
    t.onkeypress(turnup, 'Up')
    t.onkeypress(turndown, 'Down')
    t.listen()

    gameon = True
    runforward()


if __name__ == '__main__':
    main()
