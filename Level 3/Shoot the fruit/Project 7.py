import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="Game developer"
gameover=False
speed_apple=6
speed_bat=4
color=(40,43,53)
apple=Actor("apple_small")
bat=Actor("bat_small")
bat.pos=WIDTH/2,HEIGHT/2
apple.pos=WIDTH/2,HEIGHT/2
score=0
center=(WIDTH/2,HEIGHT/2)
def draw():
    global score ,gameover
    screen.clear()
    screen.fill(color)
    screen.draw.text("Shoot the fruit press q to quit",((WIDTH/2)-40,10))
    screen.draw.text(f"Score: {score}",((WIDTH/2)-390,9))
    apple.draw()
    bat.draw()
    if gameover:
        screen.clear()
        screen.fill("white")
        screen.draw.text("Game over",center=center,fontname="font",fontsize=60,color="black",gcolor="red")
        screen.draw.text("You killed the animal you lost",center=(WIDTH/2,HEIGHT/2+50),fontname="font",fontsize=30,color="black",gcolor="red")
def on_mouse_down(pos):
    global color,score,gameover
    if bat.collidepoint(pos):
        gameover=True
        sounds.emotional_damage.play()
    if apple.collidepoint(pos):
        sounds.pew.play()
        apple.pos=(random.randint(0,WIDTH))/2,(random.randint(0,HEIGHT))/2
        bat.pos=(random.randint(0,WIDTH))/2,(random.randint(0,HEIGHT))/2
        score+=10
    else:
        sounds.off.play()
        score-=5
def update():
    global gameover,score
    if keyboard.R:
        score=0
        gameover=False
    if keyboard.Q:
        print(f"You have {score} points")
        quit()
    apple.x+=speed_apple
    bat.x-=speed_bat
    if bat.x<0:
        bat.x=WIDTH
    if apple.x>=WIDTH:
        apple.x=0
# music.play("background")
pgzrun.go()