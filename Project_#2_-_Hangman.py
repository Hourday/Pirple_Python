r=""
turn = 1
length=0
import turtle
from os import system
def drawMyBuoy(turn):
    if turn==1:
        turtle.left(90)
        turtle.forward(200)   # move 1
        turtle.left(90)
    elif turn == 2:
        turtle.forward(200)   # move 2
        turtle.left(90)
    elif turn == 3:
        turtle.forward(80)   # move 3
        turtle.right(90)
        turtle.penup()
        turtle.forward(2)
        turtle.pendown()
    elif turn == 4:
        turtle.circle(10) #4 head is built
        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()
    elif turn == 5:
        turtle.forward(20) #5 throat
        turtle.left(90)
    elif turn == 6:
        turtle.forward(20) #6   1 hand
        turtle.left(180)
        turtle.forward(40)
        turtle.right(180)
    elif turn == 7:
        turtle.forward(20) #7   2nd hand
        turtle.right(90)
    elif turn == 8:
        turtle.forward(20) #8    core
        turtle.left(30)
    elif turn == 9:
        turtle.forward(20)  #9     leg 1
        turtle.left(180)
        turtle.forward(20)
        turtle.left(120)
    elif turn == 10:
        turtle.forward(20)  #10  leg 2
        turtle.left(180)
        turtle.forward(20)
    elif turn>10:
        turtle.done()
# Function to check if a key is present in the dictionary
def ispresent(dict, key):
    if key in dict.keys():
        return True
    else:
        return False
def clear(n):
    if n==True:
        _=system("cls")
    else:
        _ = system("cls")
word=input("enter your word player 1:")
token=len(word)
n=True
clear(n)
##########################################################
# put this in a separate function
lookup = {}
# create a dicionary to test if a letter is present or not
# lookup[word[i]] = true | false
for index in range(len(word)):
    lookup[word[index]] = True
##########################################################
while(True):
    if turn==11:
        print("\n\t\tYOU FAILED TO SAVE HIM \n\n\t\t**************GAME-OVER**************")
        break
    print("\nGuess the word, letter by letter: ")
    guess = input()
    #    raise Exception("Invalid input, should add only one character")
    if ispresent(lookup, guess):
       # print(lookup)
        for x in word:
            if x==guess:
                print(guess,end=" ")
            else:
                print(" _ ",end=" ")
        length=length+1
        if length==token:
            print(" \n\n \t\t **************YOU-WIN**************")
            break
    else:
        for x in word:
            if x == guess:
                print(guess, end=" ")
            else:
                print(" _ ", end=" ")
        drawMyBuoy(turn)
        turn = turn + 1



