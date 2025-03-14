import pgzrun
import random
WIDTH=800
HEIGHT=530
TITLE="ROCKET VS ASTEROIDS"
gameover=False
sound_played=False
Rocket=Actor("rocket_small")
Rocket.pos=(WIDTH/2,HEIGHT-20)
enemies=[]
speed=4
bg="background"
def draw():
    if gameover:
        screen.clear()
        screen.fill("black")
        screen.draw.text("GAME OVER",fontname="font",fontsize=90,color="white",gcolor="red",center=(WIDTH/2,HEIGHT/2))
    else:
        screen.clear()
        screen.fill("black")
        Rocket.draw()
        for enemy in enemies:
            enemy.draw()
def enemyspawn():
    Asteroid=Actor("coin")
    Asteroid.pos=random.randint(1,WIDTH),0
    enemies.append(Asteroid)
enemyspawn()
def update():
    global gameover,enemies,sound_played
    if keyboard.Left and Rocket.x > 0:
        Rocket.x -= speed
    if keyboard.Right and Rocket.x < WIDTH:
        Rocket.x += speed
    for enemy in enemies:
        if Rocket.colliderect(enemy):
            enemies.remove(enemy)
            enemies.clear()
            if not sound_played:
                sounds.homaron2.play()
                sound_played=True
            music.stop()
            gameover=True
        enemy.y+=2
        if enemy.y>HEIGHT:
            enemies.remove(enemy)
    if keyboard.Q:
        quit()
    if keyboard.R:
        gameover=False
        music.play("aura")
        sound_played=False
clock.schedule_interval(enemyspawn,0.3)
music.play("aura")
pgzrun.go()