from game import *
from xoLibrary import *
from time import sleep
from random import random, randint

clear()
print("{:<}{:^2}{:>}".format("<"*17, " ", ">"*17))
print("{:<}{:^16}{:>}".format(">"*10, "Good-Morning", "<"*10))
print("{:<}{:^2}{:>}".format("<"*17, " ", ">"*17))


while True:

    sleep(1.3)
    printMenu()
    # while(True):
    while True:
        try:
            action = int(input(">> "))
        except ValueError:
            pass
        else:
            if action in range(1, Menulenght()+1):
                break
########################################################################################################
    if action == 1:
        print(">> Player 1 choose ==>  X / O ")
        signe = input(">> ").upper()
        while signe not in ["X", "O"]:
            signe = input(">> ").upper()

        sleep(0.5)
        print(">> Player 1 ==>  {} ".format(signe))
        print(">> Player 2 ==>  {} ".format(
            ["X", "O"][(["X", "O"].index(signe)+1) % 2]))

        game = Game(signe, ["X", "O"]
                    [(["X", "O"].index(signe)+1) % 2])
        sleep(3)
        clear()

        # gameSession(game, signe, ["X", "O"][(["X", "O"].index(signe)+1) % 2])
        while True:
            gameSession(game, signe, ["X", "O"]
                        [(["X", "O"].index(signe)+1) % 2])
            if gameOver(game):
                break

        sleep(2)
        print("{:<}{:^16}{:>}".format(">"*10, "GaMe-oVeR", "<"*10))
        theWinner = game.getWinner()
        if game.getWinner(theWinner):
            print(f"Congrat {theWinner[1]} ")
        else:
            print(f"equalize")

        sleep(1.2)
        print("Do You Want To Save The Game !! y/n")
        choice = input(">> ").lower()
        while choice not in ['y', 'n']:
            choice = input(">> ").lower()

        if choice == 'y':
            print("Game Name : ")
            while True:
                gameName = input("====>> ").strip()
                if not gameName or gameName != '\n':
                    break
            saveGame(choice, game)
            del gameName

        del game
        del signe
        del action
        del choice
        del theWinner
########################################################################################################
    elif action == 2:
        if historyNotEmpty():
            sleep(0.5)
            clear()
            print("{:<}{:^16}{:>}".format(">"*10, "LoAd-GaMe", "<"*10))
            printGamesList()
            while True:
                print(">> what GaMe u wanna laod !! <<")
                while True:
                    gameName = input(">> ").strip().lower()
                    if not gameName and gameName != '\n':
                        break

                if relaodGame(gameName):
                    if game.getGameState():
                        print("HH wllh mankamell")
                    else:
                        sleep(1)
                        print("The GaMe uR siking is Completed :) !")
                        printGameInformation(game)

                else:
                    print("<<<< OoOps!! there isn't such game >>>>")
                    print("<<<< Do u wanna still relaod the game!! y/n >>>>")
                    while True:
                        choice = input(">> ").lower()
                        if choice in ['y', 'n']:
                            break
                    if choice == 'n':
                        break
            del choice
            del gameName
        else:
            sleep()
            print("U Played No GaMeS Yet ;)")
########################################################################################################
    elif action == 3:
        if historyNotEmpty():
            clear()
            game = getLastGame()
            game.showTurnsHistory(1)
        else:
            print("Nop, akkach\n")

########################################################################################################
    else:
        break

printDelay("\n\n{:<}{:^2}{:>}".format("<"*17, " ", ">"*17), 2, 2, 1)
printDelay("{:<}{:^16}{:>}".format(
    ">"*10, "Good-bYe :)", "<"*10, delayafter=1.5))
printDelay("{:<}{:^2}{:>}".format("<"*17, " ", ">"*17), delayafter=1.5)

# Start 09 : 16
# pause 11 : 20 => 2h4m
# Start 12 : 22
# pause 01 : 52 => 1h30mn
# Start 11 : 47
# pause 12 : 01 => 0h14m
# Start 12 : 23
# pause 14 : 39 => 2h16mn
# Start 17 : 32
# pause 17 : 34 => 0h2mn
# ----------------------->> 6hmn36
# Start 05 : 44
# pause 07 : 43 => 2h
# Start 21 : 00
# pause 21 : 27 => 0h27mn
# Start 23 : 00
# pause 12 : 00 => 1h
# ----------------------->> 3h27mn
# Start 18 : 00
# pause 18 : 20 => 0h20mn
# Start 18 : 48
# pause 20 : 20 => 2h32mn
# Start 12 : 20
# pause 12 : 40 => 0h20mn
# ----------------------->> 3h39mn
# Start 12 : 52
# pause =>
# Start 
# pause => 0h30mn
# Start
# pause =>

# >>>>>>>> In totall : 13h40mn
