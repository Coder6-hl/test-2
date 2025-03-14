import pgzrun
import random
WIDTH=1280
HEIGHT=720
bg="background"
TITLE="Who Wants To Be A Millionare"
center=WIDTH/2,HEIGHT/2
start=False
done_time=False
done_skip=False
done_removing=False
winner=False
gameover=False
not_right=False
sound_played=False
count_down=10
number_of_questions=1
current_question=""
main=Rect((50,40),(800,240))
answer_boxes=[Rect((50,358),(430,155)),
              Rect((520,358),(430,155)),
              Rect((50,538),(430,155)),
              Rect((520,538),(430,155))]
add_time=Rect((870,30),(100,100))
remove_2_answers=Rect((870,140),(100,100))
skip=Rect((870,250),(100,100))
circle_box=Rect((1110,130),(150,150))
highlight=Rect((1025,680),(180,30))
money=["0$","1,000$","2,000$","6,000$","16,000$","32,000$","64,000$","125,000$","250,000$","500,000$","1,000,000$"]
question=[("What is the capital of France?",["London","Paris","Berlin","Tokyo"],1)]
with open(r"E:\Programming\Level 3\Who Wants To Be a Millionare\questions.txt") as file:
    questions=file.readlines()
    for index,line in enumerate(questions):
        questions[index]=line.strip().split(",")
current_question=random.choice(questions)
questions.remove(current_question)
def draw():
    global start,current_question,done_skip,done_removing,done_time
    if gameover:
        screen.clear()
        screen.blit(bg,(0,0))
        screen.draw.text("Game over",fontname="font",fontsize=120,color="black",gcolor="red",center=(WIDTH/2,HEIGHT/2))
        music.stop()
    else:
        screen.clear()
        screen.blit(bg,(0,0))
        screen.draw.text("START?",color="black",gcolor="yellow",fontsize=400,center=center)
        if start:
            screen.clear()
            screen.blit(bg,(0,0))
            screen.draw.filled_circle((1110,130),100,"golden rod")
            screen.draw.textbox(f"{count_down}",circle_box,color="white",center=(1110,140))
            if not done_time:
                screen.draw.filled_rect(add_time,"red")
                screen.draw.textbox("Add 10sec",add_time,color="white")
            else:
                screen.draw.filled_rect(add_time,"red")
            if not done_removing:
                screen.draw.filled_rect(remove_2_answers,"red")
                screen.draw.textbox("Remove 2 answers",remove_2_answers,color="white")
            else:
                screen.draw.filled_rect(remove_2_answers,"red")
            if not done_skip:
                screen.draw.filled_rect(skip,"red")
                screen.draw.textbox("Skip",skip,color="white")
            else:
                screen.draw.filled_rect(skip,"red")
            for _ in question:
                screen.draw.filled_rect(main,"light blue")
                screen.draw.textbox(f"{current_question[0]}",main,color="white")
            for index,choice in enumerate(answer_boxes):
                    screen.draw.filled_rect(choice,"midnight blue")
                    screen.draw.textbox(f"{current_question[index+1]}",choice,color="white")
            screen.draw.filled_rect(highlight,color="orange")
            for index,dollars in enumerate(money):
                screen.draw.text(f"{dollars}",center=(1110,695-43*index),fontsize=50,color="white")
            if number_of_questions==12:
                win()
            if winner:
                screen.clear()
                screen.blit(bg,(0,0))
                screen.draw.text("Winner",fontsize=120,center=(WIDTH/2,HEIGHT/2),color="yellow",gcolor="black")
                music.stop()


def on_mouse_down(pos):
    global start,current_question,count_down,number_of_questions,done_time,done_removing,done_skip,sound_played
    if not start:
        start=True
        clock.schedule_interval(counter,1)
        music.play("background")
    if answer_boxes[0].collidepoint(pos):
        music.stop()
        if "0"==current_question[5]:
            if not sound_played:
                sounds.wait.play()
                sound_played=True
                clock.unschedule(counter)
            clock.schedule(next_queston,5)
        else:
            endgame()
    if answer_boxes[1].collidepoint(pos):
        music.stop()
        if "1"==current_question[5]:
            if not sound_played:
                sounds.wait.play()
                sound_played=True
                clock.unschedule(counter)
            clock.schedule(next_queston,5)
        else:
            endgame()
    if answer_boxes[2].collidepoint(pos):
        music.stop()
        if "2"==current_question[5]:
            if not sound_played:
                sounds.wait.play()
                sound_played=True
                clock.unschedule(counter)
            clock.schedule(next_queston,5)
        else:
            endgame()
    if answer_boxes[3].collidepoint(pos):
        music.stop()
        if "3"==current_question[5]:
            if not sound_played:
                sounds.wait.play()
                sound_played=True
                clock.unschedule(counter)
            clock.schedule(next_queston,5)
        else:
            endgame()
    if add_time.collidepoint(pos) and not done_time:
        count_down+=10
        done_time=True
    if skip.collidepoint(pos) and not done_skip:
        next_queston()
        count_down=10
        done_skip=True
def next_queston():
    global current_question,number_of_questions,count_down,highlight,sound_played
    current_question=random.choice(questions)
    number_of_questions+=1
    count_down=10
    highlight.move_ip(0,-43)
    clock.schedule_interval(counter,1)
    music.play("background")
    sound_played=False
def win():
    global winner,sound_played
    if not sound_played:
        sounds.snopp.play()
        clock.unschedule(counter)
        sound_played=True
    winner=True
def counter():
    global count_down
    count_down-=1
    if count_down<0:
        endgame()
def endgame():
    global gameover,sound_played
    if not sound_played:
        sounds.wasted.play()
        sound_played=True
    gameover=True
    clock.unschedule(counter)
def update():
    global gameover,sound_played,start,number_of_questions,winner,done_time,done_skip,done_removing,not_right,highlight,count_down
    if keyboard.Q:
        quit()
    if keyboard.R:
        start=False
        done_time=False
        done_skip=False
        done_removing=False
        winner=False
        gameover=False
        not_right=False
        sound_played=False
        number_of_questions=1
        highlight=Rect((1025,680),(180,30))
        count_down=10
pgzrun.go() 