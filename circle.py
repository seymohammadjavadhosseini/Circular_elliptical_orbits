import pgzrun

WIDTH = 700

HEIGHT = 700

jupiter = Actor("jupiter")

jupiter.angle = 0

jupiter.speed = 1

A = WIDTH / 2

B = WIDTH / 2

r = WIDTH / 2

x = 0

y = 0

flag = True

def update():
    update_jupiter()

def update_jupiter():
    global x , y , flag

    jupiter.angle += jupiter.speed
    jupiter.pos = x , y
    
    if flag:
        
        if x >= A - r and x <= r + A:
            y = (r ** 2 - (x - A) ** 2) ** (0.5) + B
            x += 10

            if x == WIDTH:
                flag = False
            print(x,y)

    else:

        if x >= A - r and x <= r + A:
            y = -(r ** 2 - (x - A) ** 2) ** (0.5) + B
            x -= 10

            if x == 0:
                flag = True
            print(x,y)

def draw():
    # screen.clear()
    jupiter.draw()

pgzrun.go()