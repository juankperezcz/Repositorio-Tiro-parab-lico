"Programa de tiro parabólico"
"Autores: Juan Carlos Pérez Collazo A01284143, Ian Becerra A01274634"
"Este juego simula un tiro parabólico utilizando una bola que destruye unas naves y es parte de la última evidencia de la semana tec:herramientas computacionales"
"Esta es la explicación de la última evidencia"
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 500) / 25
        speed.y = (y + 500) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        #Se aumentó la velocidad de los targets
        target.x -= 3

    if inside(ball):
        #Se aumentó la velocidad de la pelota
        speed.y -= 0.75
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x = 199 #se quita el return, que originalmente hace que se termine el juego y se cambia a un valor nuevo de x.
            
    ontimer(move, 10) #se disminuye el número para aumentar el movimiento

    
    

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()