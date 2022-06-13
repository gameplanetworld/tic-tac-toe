####Tic tac toe game
####Made by GamePlanetWorld

###imports
import os

###varibles
global start
start = True
global wh
wh = True
global a1
a1 = " "
global a11
a11 = False
global a2
a2 = " "
global a22
a22 = False
global a3
a3 = " "
global a33
a33 = False
global b1
b1 = " "
global b11
b11 = False
global b2
b2 = " "
global b22
b22 = False
global b3
b3 = " "
global b33
b33 = False
global c1
c1 = " "
global c11
c11 = False
global c2
c2 = " "
global c22
c22 = False
global c3
c3 = " "
global c33
c33 = False
global player1
player1 = True
global player2
player2 = False

###code
while start == True:

    print("""

 _    _         _                  _                
| |_ (_)  ___  | |_   __ _   ___  | |_   ___    ___ 
| __|| | / __| | __| / _` | / __| | __| / _ \  / _ /
| |_ | || (__  | |_ | (_| || (__  | |_ | (_) ||  __/
 \__||_| \___|  \__| \__,_| \___|  \__| \___/  \___|
                                                    
                                                    \n""")

    print("[1] PLay 2 player\n")

    userinput = input()

    if userinput == "1":
        os.system("clear")
        while wh == True:
            if a1 and a2 and a3 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False
                    start = False
                    continue
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
                    continue
            if b1 and b2 and b3 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if c1 and c2 and c3 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a1 and b1 and c1 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a2 and b2 and c2 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a3 and b3 and c3 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a1 and b2 and c3 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a3 and b2 and c1 == "x":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a1 and a2 and a3 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if b1 and b2 and b3 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if c1 and c2 and c3 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a1 and b1 and c1 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a2 and b2 and c2 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a3 and b3 and c3 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a1 and b2 and c3 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False
            if a3 and b2 and c1 == "o":
                os.system("clear")
                if player1 == True:
                    print("Player2 won!!")
                    wh = False 
                    start = False
                if player2 == True:
                    print("Player1 won!!")
                    wh = False 
                    start = False

            if player1 == True:
                print("Player 1 turn\n")
            if player2 == True:
                print("Player 2 turn\n")
            #bord
            print("|-----------|")
            print("|", c1, "|", c2, "|", c3, "|")
            print("|-----------|")
            print("|", b1, "|", b2, "|", b3, "|")
            print("|-----------|")
            print("|", a1, "|", a2, "|", a3, "|")
            print("|-----------|")
            #userinputs
            userinput2 = input()
            if userinput2 == "a1":
                if a11 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        a1 = "x"
                        player1 = False
                        player2 = True
                        a11 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        a1 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "a2":
                if a22 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        a2 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        a2 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "a3":
                if a33 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        a3 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        a3 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "b1":
                if b11 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        b1 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        b1 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "b2":
                if b22 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        b2 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        b2 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "b3":
                if b33 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        b3 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        b3 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "c1":
                if c11 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        c1 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        c1 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "c2":
                if c22 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        c2 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        c2 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            if userinput2 == "c3":
                if c33 == True:
                    os.system("clear")
                    print("that spot is already taken\n")
                    continue
                else:
                    if player1 == True:
                        c3 = "x"
                        player1 = False
                        player2 = True
                        os.system("clear")
                        continue
                    if player2 == True:
                        c3 = "o"
                        player1 = True
                        player2 = False
                        os.system("clear")
                        continue
            else:
                print("that is not a placement")
                print("press any key to return")
                input()
                os.system("clear")
                continue