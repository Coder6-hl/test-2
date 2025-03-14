import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="collect the fruit"
gameover=False
center=WIDTH/2,HEIGHT/2
fruits=["apple","apricot","banana","black grapes","blueberry","blackberry","cantelope",
        "cherry","coconut","fig 1","fig 2","green apple","green grapes","guava","kiwi",
        "lemon","lime","mango","orange","peach","pineapple","pomegranate 1","pomegranate 2",
        "raspberry","red grapes","strawberry","tangerine","watermelon"]
speed_fruits=[]
targets=[]
basket=Actor("bucket")
show=False
basket.pos=(WIDTH/2,HEIGHT-30)
bg="background"
score=0
speed=8
time=30
def draw():
    if gameover:
        screen.clear()
        screen.blit(bg,(0,0))
        screen.draw.text("GAME OVER",fontname="font",fontsize=100,center=center,color="black",gcolor="red")
        clock.unschedule(create_fruits)
        if show:
            screen.draw.text(f"Score:{score}",(WIDTH/2-80,HEIGHT/2+150),fontsize=60,color="black")
    else:
        screen.clear()
        screen.blit(bg,(0,0))
        screen.draw.text(f"Score:{score}",(10,10))
        screen.draw.text(f"Time left:{time}",(WIDTH-150,10),color="black",fontsize=30)
        basket.draw()
        for fruit in targets:
            fruit.draw()
def create_fruits():
    global fruits
    fruit=Actor(random.choice(fruits))
    fruit.pos=(random.randint(0,WIDTH),0)
    targets.append(fruit)
    speed_fruits.append(2)
def remove_fruit():
    for fruit in targets:
        targets.remove(fruit)
def show_score():
    global show
    show=True
def timer():
    global time
    time-=1
    if time==0:
        endgame()
def endgame():
    global gameover
    gameover=True
    clock.schedule(show_score,4.5)
def update():
    global score,fruits
    for fruit in targets:
        fruit.y+=speed_fruits[0]
        if basket.colliderect(fruit):
            score+=20
            targets.remove(fruit)
        if fruit.y>HEIGHT:
            score-=10
            targets.remove(fruit)
    if keyboard.Right:
        basket.x+=speed
    if keyboard.Left:
        basket.x-=speed
    if keyboard.Q:
        quit()
clock.schedule_interval(create_fruits,1)
clock.schedule_interval(timer,1)
music.play("next")
pgzrun.go()