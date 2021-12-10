from turtle import *
from random import randint
from random import shuffle
import winsound
from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import numpy as np
import os

winsound.PlaySound('Judas.wav',winsound.SND_ASYNC + winsound.SND_LOOP)

backcol="#97F0F0"
bgcolor(backcol)
title("Racing Game - GROUP 01")
speed(50)

decorate=Turtle()
decorate.penup()
decorate.goto(-290,220)
decorate.pendown()
decorate.color('green')
decorate.write("GAME RACING",font=("Jokerman",20))
decorate.penup()
decorate.goto(-290,180)
decorate.pendown()
decorate.color('red')
decorate.write("GROUP 01", font=("Chiller",20))
decorate.color(backcol)

class Character:
    def __init__ (self,shapeOfCharacter,ColorOfCharacter):
        self.character = Turtle()
        self.character.color(ColorOfCharacter)
        self.character.shape(shapeOfCharacter)

    def DanceOfWinner(self,step):
        self.character.left(50)
        self.character.forward(5)
        for i in range(step):
            self.character.right(100)
            self.character.forward(5)
            self.character.left(100)
            self.character.forward(5)

playername=textinput("Player's Name - Group 01","\nPlease enter your name     \n")

#choose race
cr=numinput('Choose Race - Group 01',
            "Which race do you want to play?     \n"
                 "1. Short Race\n"
                 "2. Medium Race\n"
                 "3. Long Race\n\n"
            "Enter 1 or 2 or 3 to choose the race")

while (cr!=1 and cr!=2 and cr!=3):
    cr=numinput('Choose Race - Group 01',
                "Which race do you want to play?     \n"
                 "1.Short Race\n"
                 "2. Medium Race\n"
                 "3. Long Race\n"
                "Enter 1 or 2 or 3 to choose the race\n\n"
                "\tPlease choose again\n")

#choose set character
cc=numinput('Choose Set Character - Group 01',
            "Which set character do you want to play?     \n"
                "1. Cat\n"
                "2. Dog\n"
                "3. Horse\n"
                "4. Lion\n"
                "5. Penguin\n\n"
            "Enter 1, 2, 3, 4 or 5 to choose the race")
while (cc!=1 and cc!=2 and cc!=3 and cc!=4 and cc!=5):
    cc = numinput('Choose Set Character - Group 01',
                  "Which set character do you want to play?     \n"
                  "1. Cat\n"
                  "2. Dog\n"
                  "3. Horse\n"
                  "4. Lion\n"
                  "5. Penguin\n"
                  "Enter 1, 2, 3, 4 or 5 to choose the race\n"
                  "\tPlease choose again\n")

#bettingCharacter
bc=numinput("Betting Character - Group 01","\nWhich color of the character do you want to bet on?\n"
                                           "\t1. Red\n\t2. Blue\n\t3. Yellow\n\t4. Green\n\t"
                                           "5. Brown\n\t6. Purple\n"
                                           "Enter 1, 2, 3, 4, 5 or 6 to choose.\n")
while (bc!=1 and bc!=2 and bc!=3 and bc!=4 and bc!=5 and bc!=6):
    bc = numinput("Betting Character - Group 01", "\nWhich color of the character do you want to bet on?\n"
                                                  "\t1. Red\n\t2. Blue\n\t3. Yellow\n\t4. Green\n\t"
                                                  "5. Brown\n\t6. Purple\n"
                                                  "Enter 1, 2, 3, 4, 5 or 6 to choose.\n"
                                                  "\tPlease choose again\n")

plname=Turtle()
plname.penup()
plname.goto(100,200)
plname.pendown()
plname.clear()
plname.write("Hello {}".format(playername), False, align = 'left', font=("Arial",14))
plname.color(backcol)

penup()
goto(-140,80)

if cr == 1:
    addshape('short race.gif')
    insertRace = Turtle()
    insertRace.penup()
    insertRace.goto(-50, -50)
    insertRace.pendown()
    insertRace.shape('short race.gif')
    lengthOfRace = 10
    dr = 255
if cr == 2:
    addshape('medium race.gif')
    insertRace = Turtle()
    insertRace.penup()
    insertRace.goto(10, -50)
    insertRace.pendown()
    insertRace.shape('medium race.gif')
    lengthOfRace = 16
    dr = 350
if cr==3:
    addshape('long race.gif')
    insertRace = Turtle()
    insertRace.penup()
    insertRace.goto(50, -45)
    insertRace.pendown()
    insertRace.shape('long race.gif')
    lengthOfRace = 20
    dr = 450

for step in range(lengthOfRace):
    if (step%2==0):
        color('black')
        write(step, align='center')
    else:
        color('red')
        write(step, align='center')
    color('grey')
    right(90)
    #forward(20)
    pendown()
    forward(300)
    penup()
    backward(300)
    left(90)
    forward(20)

x=-160
y=58
dis=48

decorRace=Turtle()
decorRace.color('white')
decorRace.speed(80)
for count in range (5):
    decorRace.penup()
    decorRace.goto(x-10,y-22-((25+dis/2)*count))
    decorRace.pendown()
    decorRace.forward(dr)
decorRace.color('grey')

if cc == 1:
    addshape('red-cat.gif')
    addshape('blue-cat.gif')
    addshape('yellow-cat.gif')
    addshape('green-cat.gif')
    addshape('brown-cat.gif')
    addshape('purple-cat.gif')
    redC = Character('red-cat.gif', 'red')
    blueC = Character('blue-cat.gif', 'blue')
    greenC = Character('green-cat.gif', 'green')
    yellowC = Character('yellow-cat.gif', 'yellow')
    brownC = Character('brown-cat.gif', 'brown')
    purpleC = Character('purple-cat.gif', 'purple')
    if cr==1:
        fwran=2
        backran=6
    if cr==2:
        fwran=2
        backran=10
    if cr==3:
        fwran = 2
        backran = 13
if cc==2:
    addshape('red-dog.gif')
    addshape('blue-dog.gif')
    addshape('yellow-dog.gif')
    addshape('green-dog.gif')
    addshape('brown-dog.gif')
    addshape('purple-dog.gif')
    redC = Character('red-dog.gif', 'red')
    blueC = Character('blue-dog.gif', 'blue')
    greenC = Character('green-dog.gif', 'green')
    yellowC = Character('yellow-dog.gif', 'yellow')
    brownC = Character('brown-dog.gif', 'brown')
    purpleC = Character('purple-dog.gif', 'purple')
    if cr==1:
        fwran=2
        backran=6
    if cr==2:
        fwran=2
        backran=10
    if cr==3:
        fwran = 2
        backran = 13
if cc==3:
    addshape('red-horse.gif')
    addshape('blue-horse.gif')
    addshape('yellow-horse.gif')
    addshape('green-horse.gif')
    addshape('brown-horse.gif')
    addshape('purple-horse.gif')
    redC = Character('red-horse.gif', 'red')
    blueC = Character('blue-horse.gif', 'blue')
    greenC = Character('green-horse.gif', 'green')
    yellowC = Character('yellow-horse.gif', 'yellow')
    brownC = Character('brown-horse.gif', 'brown')
    purpleC = Character('purple-horse.gif', 'purple')
    if cr==1:
        fwran=1
        backran=7
    if cr==2:
        fwran=2
        backran=10
    if cr==3:
        fwran = 2
        backran = 13
if cc==4:
    addshape('red-lion.gif')
    addshape('blue-lion.gif')
    addshape('yellow-lion.gif')
    addshape('green-lion.gif')
    addshape('brown-lion.gif')
    addshape('purple-lion.gif')
    redC = Character('red-lion.gif', 'red')
    blueC = Character('blue-lion.gif', 'blue')
    greenC = Character('green-lion.gif', 'green')
    yellowC = Character('yellow-lion.gif', 'yellow')
    brownC = Character('brown-lion.gif', 'brown')
    purpleC = Character('purple-lion.gif', 'purple')
    if cr==1:
        fwran = 3
        backran = 5
    if cr==2:
        fwran = 3
        backran = 9
    if cr==3:
        fwran = 3
        backran = 12
if cc==5:
    addshape('red-penguin.gif')
    addshape('blue-penguin.gif')
    addshape('yellow-penguin.gif')
    addshape('green-penguin.gif')
    addshape('brown-penguin.gif')
    addshape('purple-penguin.gif')
    redC = Character('red-penguin.gif', 'red')
    blueC = Character('blue-penguin.gif', 'blue')
    greenC = Character('green-penguin.gif', 'green')
    yellowC = Character('yellow-penguin.gif', 'yellow')
    brownC = Character('brown-penguin.gif', 'brown')
    purpleC = Character('purple-penguin.gif', 'purple')
    if cr==1:
        fwran = 3
        backran = 5
    if cr==2:
        fwran = 4
        backran = 9
    if cr==3:
        fwran = 5
        backran = 11

list = [1, 2, 3, 4, 5, 6]
shuffle(list)
colorlist = [redC, blueC, yellowC, greenC, brownC, purpleC]
shuffle(colorlist)

for i in range(0, 6):
    #colorlist[i].shape('turtle')
    colorlist[i].character.penup()
    colorlist[i].character.goto(x, y - dis*int(list[i]-1))
    colorlist[i].character.pendown()

sumrace1,sumrace2,sumrace3,sumrace4,sumrace5,sumrace6=0,0,0,0,0,0
for turn in range(50):
    ran1,ran2,ran3,ran4,ran5,ran6=randint(fwran,backran),randint(fwran,backran),randint(fwran,backran),randint(fwran,backran),randint(fwran,backran),randint(fwran,backran)
    redC.character.forward(ran1)
    blueC.character.forward(ran2)
    yellowC.character.forward(ran3)
    greenC.character.forward(ran4)
    brownC.character.forward(ran5)
    purpleC.character.forward(ran6)
    sumrace1+=ran1
    sumrace2+=ran2
    sumrace3+=ran3
    sumrace4+=ran4
    sumrace5+=ran5
    sumrace6+=ran6

def findMaxSumrace(sumrace1,sumrace2,sumrace3,sumrace4,sumrace5,sumrace6):
    max=sumrace1
    if (max<sumrace2):
        max=sumrace2
    if (max<sumrace3):
        max=sumrace3
    if (max<sumrace4):
        max=sumrace4
    if (max<sumrace5):
        max=sumrace5
    if (max<sumrace6):
        max=sumrace6
    return max

max=findMaxSumrace(sumrace1,sumrace2,sumrace3,sumrace4,sumrace5,sumrace6)

redC.character.forward(max-sumrace1)
blueC.character.forward(max-sumrace2)
yellowC.character.forward(max-sumrace3)
greenC.character.forward(max-sumrace4)
brownC.character.forward(max-sumrace5)
purpleC.character.forward(max-sumrace6)

stepDance=10
if (sumrace1==max):
    redC.DanceOfWinner(stepDance)
if (sumrace2==max):
    blueC.DanceOfWinner(stepDance)
if (sumrace3==max):
    yellowC.DanceOfWinner(stepDance)
if (sumrace4==max):
    greenC.DanceOfWinner(stepDance)
if (sumrace5==max):
    brownC.DanceOfWinner(stepDance)
if (sumrace6==max):
    purpleC.DanceOfWinner(stepDance)

file = open("result.txt", "r")
countWin = int(file.readline())
countLose = int(file.readline())
file.close()
os.remove("result.txt")

def findWinner(sumrace1,sumrace2,sumrace3,sumrace4,sumrace5,sumrace6,max,bc):
    if (max == sumrace1):
        winner='red'
        cw=1
    if (max==sumrace2):
        winner='blue'
        cw=2
    if (max==sumrace3):
        winner='yellow'
        cw=3
    if (max==sumrace4):
        winner='green'
        cw=4
    if (max==sumrace5):
        winner='brown'
        cw=5
    if (max==sumrace6):
        winner='purple'
        cw=6

    # Cửa sổ chính
    output = "          TOTAL SCORE\n\nRED\t\t {}\nBLUE\t\t {}\nYELLOW\t\t {}\nGREEN\t\t {}\nBROWN\t\t {}\nPURPLE\t\t {}\n\nThe winner is: {}".format(sumrace1,sumrace2,sumrace3,sumrace4,sumrace5,sumrace6,winner)
    if (bc==cw):
        output+='\n\nCongratulation! Your character is winner :)\n'
    else:
        output+='\n\nOops! Your character is loser :(\n'
    output += '\n\nThanks for playing our game\n\n-----GROUP 01-----\n'
    #with open('result.txt', 'w') as the_file:
        #the_file.write('{}\n{}'.format(countWin,countLose))
    tkinter.messagebox.showinfo("RESULT - Racing Game - Group 01", output)
    return cw

cw=findWinner(sumrace1,sumrace2,sumrace3,sumrace4,sumrace5,sumrace6,max,bc)

if (bc==cw):
    countWin+=1
else:
    countLose+=1

totalCount=countLose+countWin

file = open("result.txt", "w")
file.write(str(countWin))
file.write('\n')
file.write(str(countLose))
file.close()

file = open("score.txt", "r")
red = int(file.readline())
blue = int(file.readline())
yellow = int(file.readline())
green = int(file.readline())
brown = int(file.readline())
purple = int(file.readline())
file.close()

os.remove("result.txt")

if cw==1:
    red+=1
if cw==2:
    blue+=1
if cw==3:
    yellow+=1
if cw==4:
    green+=1
if cw==5:
    brown+=1
if cw==6:
    purple+=1

labels = 'Win','Lose'
sizes = [countWin/totalCount, countLose/totalCount]
explode = (0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

objects = ('Red', 'Blue', 'Yellow', 'Green', 'Brown', 'Purple')
y_pos = np.arange(len(objects))
performance = [red,blue,yellow,green,brown,purple]
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('games')
plt.title('Numbers of winning game of each character')
plt.show()

with open('result.txt', 'w') as the_file:
    the_file.write('{}\n{}'.format(countWin,countLose))
with open('score.txt', 'w') as the_file:
    the_file.write('{}\n{}\n{}\n{}\n{}\n{}'.format(red,blue,yellow,green,brown,purple))

done()