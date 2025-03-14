import pgzrun
import random
WIDTH=800
HEIGHT=600
TITLE="EGG Catcher"
bg="dungeon"
player=Actor("hero")
player.pos=(200,300)
eggs=0
Health=3
speed=3
win=False
sound_played=False
awake_easy=False
awake_meduim=False
awake_hard=False
gameover=False
enemeies=[]
Egg_collected=Actor("egg-count")
Egg_collected.pos=(10,HEIGHT-40)
Health_indicator=Actor("life-count")
Health_indicator.pos=(90,HEIGHT-35)
easy={"dragon":Actor("dragon-asleep",pos=(600,100)),"egg":Actor("one-egg",pos=(400,100)),"a/h":True,"interval_needed":6,"interval":0,"sleep":8,"count":0}
enemeies.append(easy)
medium={"dragon":Actor("dragon-asleep",pos=(600,300)),"egg":Actor("two-eggs",pos=(400,300)),"a/h":True,"interval_needed":4,"interval":0,"sleep":6,"count":0}
enemeies.append(medium)
hard={"dragon":Actor("dragon-asleep",pos=(600,500)),"egg":Actor("three-eggs",pos=(400,500)),"a/h":True,"interval_needed":2,"interval":0,"sleep":4,"count":0}
enemeies.append(hard)
def draw():
    if not gameover:
        screen.clear()
        screen.blit(bg,(0,0))
        player.draw()
        Egg_collected.draw()
        Health_indicator.draw()
        screen.draw.text(f"{eggs}",(40,HEIGHT-50),fontname="font")
        screen.draw.text(f"{Health}",(125,HEIGHT-50),fontname="font")
        create_dragons()
    if win:
        screen.clear()
        screen.fill("black")
        screen.draw.text("YOU WON",fontname="font",fontsize=60,color="white",gcolor="yellow",center=(WIDTH/2,HEIGHT/2))
        screen.draw.text(f"EGG collected:{eggs}",(WIDTH/2-150,HEIGHT/2+100),fontname="font",fontsize=40,color="white",gcolor="yellow")
    if gameover:
        screen.clear()
        screen.fill("black")
        screen.draw.text("GAME OVER",fontname="font",fontsize=60,color="white",gcolor="red",center=(WIDTH/2,HEIGHT/2))
        screen.draw.text(f"EGG collected:{eggs}",(WIDTH/2-150,HEIGHT/2+100),fontname="font",fontsize=40,color="white",gcolor="red")
def create_dragons():
    for enemy in enemeies:
        enemy["dragon"].draw()
        if enemy["a/h"]==True:
            enemy["egg"].draw()
def wake_up_easy():
    enemeies[0]["dragon"]=Actor("dragon-awake",pos=(570,100))
    sounds.dragon_fire.play()
def sleep_tight_easy():
    enemeies[0]["dragon"]=Actor("dragon-asleep",pos=(570,100))
def wake_up_meduim():
    enemeies[1]["dragon"]=Actor("dragon-awake",pos=(570,300))
    sounds.dragon_fire.play()
def sleep_tight_meduim():
    enemeies[1]["dragon"]=Actor("dragon-asleep",pos=(600,300))
def wake_up_hard():
    enemeies[2]["dragon"]=Actor("dragon-awake",pos=(600,500))
    sounds.dragon_fire.play()
def sleep_tight_hard():
    enemeies[2]["dragon"]=Actor("dragon-asleep",pos=(600,500))
def check():
    global awake_easy,awake_hard,awake_meduim
    enemeies[0]["interval"]+=1
    enemeies[0]["count"]+=1
    if enemeies[0]["interval_needed"]==enemeies[0]["interval"]:
        awake_easy=True
        enemeies[0]["interval"]=0
    if enemeies[0]["sleep"]==enemeies[0]["count"]:
        enemeies[0]["count"]=0
        awake_easy=False
    if awake_easy:
        wake_up_easy()
    if not awake_easy:
        sleep_tight_easy()
    enemeies[1]["interval"]+=1
    enemeies[1]["count"]+=1
    if enemeies[1]["interval_needed"]==enemeies[1]["interval"]:
        awake_meduim=True
        enemeies[1]["interval"]=0
    if enemeies[1]["sleep"]==enemeies[1]["count"]:
        enemeies[1]["count"]=0
        awake_meduim=False
    if awake_meduim:
        wake_up_meduim()
    if not awake_meduim:
        sleep_tight_meduim()
    enemeies[2]["interval"]+=1
    enemeies[2]["count"]+=1
    if enemeies[2]["interval_needed"]==enemeies[2]["interval"]:
        awake_hard=True
        enemeies[2]["interval"]=0
    if enemeies[2]["sleep"]==enemeies[2]["count"]:
        enemeies[2]["count"]=0
        awake_hard=False
    if awake_hard:
        wake_up_hard()
    if not awake_hard:
        sleep_tight_hard()
def egg_returner():
    if enemeies[0]["a/h"]==False:
        clock.schedule(return_eggs_easy,3.0)
    if enemeies[1]["a/h"]==False:
        clock.schedule(return_eggs_meduim,3.0)
    if enemeies[2]["a/h"]==False:
        clock.schedule(return_eggs_hard,3.0)
def return_eggs_easy():
        enemeies[0]["a/h"]=True
        sounds.egg_respawned.play()
def return_eggs_meduim():
        enemeies[1]["a/h"]=True
        sounds.egg_respawned.play()
def return_eggs_hard():
        enemeies[2]["a/h"]=True
        sounds.egg_respawned.play()
def endgame():
    global gameover,sound_played
    gameover=True
    music.stop()
    if not sound_played:
        sounds.game_over.play()
        sound_played=True
    clock.unschedule(check)
    clock.unschedule(egg_returner)
def winner():
    global win,sound_played
    win=True
    music.stop()
    if not sound_played:
        sounds.game_win.play()
        sound_played=True
    clock.unschedule(check)
    clock.unschedule(egg_returner)
def update():
    global eggs,Health,sound_played,win,gameover
    if eggs>=10:
        winner()
    if Health==0:
        endgame()
    if not gameover:
        if enemeies[0]["dragon"].image=="dragon-awake":
            if player.colliderect(enemeies[0]["dragon"]):
                sounds.hero_hit.play()
                player.pos=(200,300)
                Health-=1
        if enemeies[1]["dragon"].image=="dragon-awake":
            if player.colliderect(enemeies[1]["dragon"]):
                sounds.hero_hit.play()
                player.pos=(200,300)
                Health-=1
        if enemeies[2]["dragon"].image=="dragon-awake":
            if player.colliderect(enemeies[2]["dragon"]):
                sounds.hero_hit.play()
                player.pos=(200,300)
                Health-=1
        if enemeies[0]["a/h"]==True:
            if player.colliderect(enemeies[0]["egg"]):
                sounds.egg_collected.play()
                enemeies[0]["a/h"]=False
                eggs+=1
        if enemeies[1]["a/h"]==True:
            if player.colliderect(enemeies[1]["egg"]):
                sounds.egg_collected.play()
                enemeies[1]["a/h"]=False
                eggs+=2
        if enemeies[2]["a/h"]==True:
            if player.colliderect(enemeies[2]["egg"]):
                sounds.egg_collected.play()
                enemeies[2]["a/h"]=False
                eggs+=3
        if keyboard.Right:
            player.x+=speed
        if keyboard.Left and not player.x<0:
            player.x-=speed
        if player.x>WIDTH:
            player.x=0
        if player.x<0:
            player.x=WIDTH
        if player.y<0:
            player.y=HEIGHT
        if player.y>HEIGHT:
            player.y=0
        if keyboard.Up:
            player.y-=speed
        if keyboard.Down and not player.y>HEIGHT:
            player.y+=speed
    if keyboard.Q:
        quit()
clock.schedule_interval(egg_returner,1)
clock.schedule_interval(check,1)
music.play("background")
pgzrun.go()