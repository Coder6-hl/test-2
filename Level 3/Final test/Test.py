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
awake_easy=False
awake_meduim=False
awake_hard=False
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
    screen.clear()
    screen.blit(bg,(0,0))
    player.draw()
    Egg_collected.draw()
    Health_indicator.draw()
    screen.draw.text(f"{eggs}",(40,HEIGHT-50),fontname="font")
    screen.draw.text(f"{Health}",(125,HEIGHT-50),fontname="font")
    create_dragons()
def create_dragons():
    for enemy in enemeies:
        enemy["dragon"].draw()
        if enemy["a/h"]==True:
            enemy["egg"].draw()
def wake_up_easy():
    enemeies[0]["dragon"]=Actor("dragon-awake",pos=(600,100))
def sleep_tight_easy():
    enemeies[0]["dragon"]=Actor("dragon-asleep",pos=(600,100))
def wake_up_meduim():
    enemeies[1]["dragon"]=Actor("dragon-awake",pos=(600,300))
def sleep_tight_meduim():
    enemeies[1]["dragon"]=Actor("dragon-asleep",pos=(600,300))
def wake_up_hard():
    enemeies[2]["dragon"]=Actor("dragon-awake",pos=(600,500))
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
    
def update():
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
clock.schedule_interval(check,1)
pgzrun.go()