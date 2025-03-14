import pgzrun
import random
gameOver=False
speed=4
WIDTH=500
HEIGHT=500
TITLE="Game developer"
bg="background"
animations=[]
fox=Actor("fox")
coin=Actor("coin")
bat=Actor("bat_small")
fox.pos=WIDTH/2,HEIGHT/2
score=0
count_down=10
# def counter():
#     global count_down
#     count_down-=1
def timeUp():
    global gameOver
    gameOver=True
def draw():
    global count_down,gameOver,score
    if not gameOver:
        screen.clear()
        screen.blit(bg,(0,0))
        screen.draw.text("Collect the coins",(WIDTH/2-100,10),fontname="wonder",fontsize=20,color="black",gcolor="green")
        screen.draw.text(f"Coins: {score}",(0,10))
        fox.draw()
        coin.draw()
        bat.draw()
        screen.draw.text(f"Time: {count_down}",(430,10))
    else:
        screen.clear()
        screen.fill("maroon")
        screen.draw.text("Game Over",(200,200))
        screen.draw.text(f"Score:{score}",(200,250))
def update():
    global score,gameOver,count_down
    if count_down<0:
        gameOver=True
    if fox.colliderect(coin):
        sounds.coin.play()
        count_down+=1
        score+=1
        coin.pos=random.randint(0,500),random.randint(0,500)
        bat.pos=random.randint(0,500),random.randint(0,500)
    if fox.colliderect(bat):
        gameOver=True
    if keyboard.Right:
        if fox.x<WIDTH:
            fox.x+=speed
        else:
            fox.x=0
    elif keyboard.Left:
        if fox.x>0:
            fox.x-=speed
        else:
            fox.x=WIDTH
    elif keyboard.Up:
        if fox.y>0:
            fox.y-=speed
        else:
            fox.y=HEIGHT
    elif keyboard.Down:
        if fox.y<HEIGHT:
            fox.y+=speed
        else:
            fox.y=0
    elif keyboard.Q:
        print(f"You have {score} Coins")
        quit()
# clock.schedule_interval(counter, 1.0)
music.play("next")
pgzrun.go()