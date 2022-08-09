from time import time, sleep
from os import system, name
from game import *

GamesHistory = {}
Menu = [
    "01. NeW GaMe",
    "02. Resume A Game",
    "03. Show Last Game Historyy",
    "04. Quit"
]

normalBoard = """
            -------------
            - {} - {} - {} -
            -------------
            - {} - {} - {} -
            -------------
            - {} - {} - {} -
            -------------
"""


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def printDelay(message, delay=0, delayafter=0, clearsc=0, clearscAfter=0):
    if clearsc:
        clear()
    sleep(delay)
    print(message)
    sleep(delayafter)
    if clearscAfter:
        clear()


def printMenu():
    for item in Menu:
        print(item)


def Menulenght():
    return len(Menu)


def boardPrinter(positions):
    print(normalBoard.format(*positions))
    # ida drt hadi bedellha tan fii xcvdfrtc
    # return normalBoard.format(*positions)


def gameOver(game):
    return not game.getGameState()


def getMove(game, pSigne):
    while True:
        try:
            position = int(input(f":: {pSigne} :: What Position! >> "))
        except ValueError:
            pass
        else:
            if 0 <= position <= 8 and game.emptyPosition(position):
                break
    return position


def updateGameSession(game, pSigne=""):
    clear()
    boardPrinter(game.getAllPosition())
    # not pSigne bach ki mndirch signe tsemma rahi mara lowla
    if pSigne and game.updateState(pSigne):
        return 1
    return 0


def gameSession(game, p1Signe, p2Signe):
    signes = [p1Signe, p2Signe]
    updateGameSession(game)

    while not gameOver(game):
        for id, signe in enumerate(signes):
            print("<< Player N-{} Turn {} >>".format(id+1, signe))
            player = getMove(game, signe)
            game.setPosition(player, signe)
            if updateGameSession(game, signe):
                break


########################################################################
def saveGame(gameName, game):
    GamesHistory[gameName] = game


def relaodGame(gameName):
    return GamesHistory.get(gameName, False)


def historyNotEmpty():
    return len(GamesHistory)


def getGameHistoryNamesList():
    return GamesHistory.keys()


def getLastGame():
    return list(GamesHistory.values())[-1]


def printGamesList():
    for gameName, Game in GamesHistory.items():
        print(f">>> {gameName} :: {Game.getAllPosition()} ")
        # print(f">>> {gameName} :: {boardPrinter(Game.getAllPosition())} ")


def printGameInformation(game):
    sleep(1)
    print("<<<<<< GaMe-information >>>>>>")
    sleep(0.5)
    print(">> GaMe sTaTe : Completed")
    sleep(0.5)
    print(f">> Player One Name : Not-Yet X) ")
    sleep(0.5)
    print(f">> Player One Signe :{game.getPlayerSigne(1)} ")
    sleep(0.5)
    print(f">> Player Two Name : Not-Yet X) ")
    sleep(0.5)
    print(f">> Player TWo Signe :{game.getPlayerSigne(2)} ")
    sleep(0.5)
    print(f">> The Winner ===> {game.getWinner()} ")
    sleep(0.5)
    print(f">>>>>>>>>>   Game BoaRd !   <<<<<<<<<<")
    sleep(1)
    boardPrinter(game.getAllPosition())
    sleep(1)

    # print(f">> The Winner ===> {game.getWinnerName()} ")


# board = """
# ----------------------------------
# -   x   x  -          -          -
# -     x    -          -          -
# -   x   x  -          -          -
# ----------------------------------
# -          -          -          -
# -          -          -          -
# -          -          -          -
# ----------------------------------
# -          -          -          -
# -          -          -          -
# -          -          -          -
# ----------------------------------"""
squar = """
------------
-          -
-          -
-          -
------------"""


# def getMove(game, pSigne, message="", player=""):
#     if not message:
#         print(message)
#     while True:
#         # while not game.emptyPosition(Player1):
#         try:
#             position = int(input(f":: {pSigne} :: What Position! >> "))
#         except ValueError:
#             pass
#         else:
#             # if 0 < L < 4:
#             # # HAdi nhar ndir ligne cologne
#             if 0 <= position <= 8 and game.emptyPosition(position):
#                 break

#     # while True:
#     # 	try:
#     # 		C = int(input("// Colone >>"))
#     # 	except ValueError:
#     # 		pass
#     # 	else:
#         # 		if 0 < C < 4:
#                 # HAdi nhar ndir ligne cologne
#     # 			break

#     # return [L, C]
#     # HAdi nhar ndir ligne cologne
#     return position


# def updateGameSession(game, pSigne, counter=0):

#     clear()
#     if counter:
#         if game.updateState(pSigne):
#             boardPrinter(game.getAllPosition())
#             return 0

#     boardPrinter(game.getAllPosition())
#     return 1


# def gameSession(game, p1Signe, p2Signe):
#     Player1 = 0
#     Player2 = 0
#     while not gameOver(game):

#     # HAdi nhar ndir ligne cologne
#     # Player1 = []
#     # Player2 = []
#     updateGameSession(game, p1Signe)

#     # xcvdfrtc
#     # board(game.getAllPosition())
#     ########################################################
#     Player1 = getMove(
#         game, p1Signe, message="<< Player One Turn {} >>".format(p1Signe))
#     # while not game.emptyPosition(Player1):
#     #     Player1 = getMove(game)
#     #     break
#     game.setPosition(Player1, p1Signe)
#     ########################################################
#     curentSessionState = updateGameSession(game, p1Signe, 1)
#     if not curentSessionState:
#         return 0
#     ########################################################
#     Player2 = getMove(
#         game, p2Signe, message="<< Player Two Turn {} >>".format(p2Signe))
#     # while not game.emptyPosition(Player2):
#     #     Player2 = getMove(game)
#     #     break
#     game.setPosition(Player2, p2Signe)
#     ########################################################
#     curentSessionState = updateGameSession(game, p1Signe, 1)
#     if not curentSessionState:
#          return 0
