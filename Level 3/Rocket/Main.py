import random 
import pgzrun
TITLE ="el project"
WIDTH = 800
HEIGHT = 600
rocket = Actor("rocket_small")
enemies=[]
speed=4
rocket.pos = (WIDTH/2,HEIGHT-30)
gameover = False
sound_played=False
def draw():
    global gameover
    if gameover:
        screen.clear()
        screen.fill("black")
        screen.draw.text("GAME OVER",fontname="font",fontsize=90,color="white",gcolor="red",center=(WIDTH/2,HEIGHT/2))
    else:
        screen.clear()
        screen.fill("black")
        rocket.draw()
        for enemy in enemies:
            enemy.draw()
def create_enemeis():
    global enemies
    Meteor=Actor("coin")
    Meteor.pos=random.randint(1,WIDTH),0
    enemies.append(Meteor)
def update():
    global enemies,gameover,sound_played
    for enemy in enemies:
        enemy.y+=speed
        if rocket.colliderect(enemy):
            enemies.remove(enemy)
            enemies.clear()
            if not sound_played:
                sounds.still.play()
                sound_played=True
            gameover=True

            music.stop()
    if keyboard.D:
        rocket.x += speed
    if keyboard.A:
        rocket.x -= speed
    if keyboard.Q:
        quit()
    if keyboard.R:
        gameover=False
        music.play("aura")
        sound_played=False
music.play("aura")
clock.schedule_interval(create_enemeis,0.4)
pgzrun.go()