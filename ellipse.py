import pgzrun

WIDTH = 1500

HEIGHT = 700

jupiter = Actor("jupiter2")

jupiter.angle = 0

jupiter.speed = 1

A = WIDTH / 2

B = HEIGHT / 2

r = HEIGHT / 2

R = WIDTH / 2

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
        
        if x >= A - R and x <= R + A:
            y = r * ((1 - ((x - A) / R)** 2) ** (0.5)) + B
            x += 10

            if x == WIDTH:
                flag = False
            print(x,y)

    else:

        if x >= A - R and x <= R + A:
            y = - r * ((1 - ((x - A) / R)** 2) ** (0.5)) + B
            x -= 10

            if x == 0:
                flag = True
            print(x,y)
        

def draw():
    # screen.clear()
    jupiter.draw()


pgzrun.go()