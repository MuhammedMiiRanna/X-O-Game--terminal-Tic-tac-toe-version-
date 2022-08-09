class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.__winner = "equalize"
        self.__winnerName = ""
        self.__gameState = True
        self.__positions = [i for i in range(0, 9)]
        self.__turnsHistory = []

    def getPlayerSigne(self, id):
        if id == 1:
            return self.p1
        return self.p2

    def getGameState(self):
        return self.__gameState

    def setGameState(self, value):
        self.__gameState = value

    def getPosition(self, index):
        return self.__positions[index]

    def getAllPosition(self):
        return self.__positions

    def setPosition(self, index, char, history = 1):
        self.__positions[index] = char
        if history :
            self.__turnsHistory.append([char, index])

    def emptyPosition(self, index):
        # if self.getPosition(index) in range(0, 9):
        if self.getPosition(index) in range(0, 9):
            return True
        return False

    def setWinner(self, winner):
        self.__winner = winner

    def getWinnerSigne(self):
        if self.__winner == "Player One":
            return self.p1
        elif self.__winner == "Player Two":
            return self.p2
        return

    def getWinner(self, winner=""):
        if self.__winner == "equalize":
            return False, "equalize"
        winner = self.__winner
        return True, self.__winner, self.getWinnerSigne()

    def showTurnsHistory(self, case=0):
        if not case:
            return self.__turnsHistory
        print("#"*25)
        for id, turns in enumerate(self.__turnsHistory):
            print("Turn N-{} :: {} played :: {} ".format(id, *turns))

    def setFinallState(self):
        for index, value in enumerate(self.__positions):
            if value not in ["X", "O"]:
                self.setPosition(index, " ", 0)

    def updateStateOneCase(self, pSigne):
        winnerSign = ""
        if pSigne == self.__positions[0] == self.__positions[1] == self.__positions[2]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[0] == self.__positions[3] == self.__positions[6]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[0] == self.__positions[4] == self.__positions[8]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[6] == self.__positions[4] == self.__positions[2]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[6] == self.__positions[7] == self.__positions[8]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[1] == self.__positions[4] == self.__positions[7]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[2] == self.__positions[5] == self.__positions[8]:
            self.setGameState(False)
            winnerSign = pSigne
        elif pSigne == self.__positions[3] == self.__positions[4] == self.__positions[5]:
            self.setGameState(False)
            winnerSign = pSigne

        return winnerSign

    def updateState(self, pSigne):
        try:
            winnerSign = self.updateStateOneCase(pSigne)
        finally:
            if self.p1 == winnerSign:
                self.setWinner("Player One")
                self.setFinallState()
            elif self.p2 == winnerSign:
                self.setWinner("Player Two")
                self.setFinallState()
            return not self.getGameState()


#############################################################################################################################################
#  def updateState(self):

#         winnerSign = ""
#         try:
#             if self.__positions[0] == "O" and self.__positions[0] == self.__positions[1] and self.__positions[0] == self.__positions[2]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[0] == self.__positions[3] and self.__positions[0] == self.__positions[6]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[0] == self.__positions[4] and self.__positions[0] == self.__positions[8]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[6] == self.__positions[4] and self.__positions[6] == self.__positions[2]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[6] == self.__positions[7] and self.__positions[6] == self.__positions[8]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[1] == self.__positions[4] and self.__positions[1] == self.__positions[7]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[2] == self.__positions[5] and self.__positions[2] == self.__positions[8]:
#                 self.setGameState(False)
#                 winnerSign = "O"
#             elif self.__positions[0] == "O" and self.__positions[3] == self.__positions[4] and self.__positions[3] == self.__positions[5]:
#                 self.setGameState(False)
#                 winnerSign = "O"

#             elif self.__positions[0] == "X" and self.__positions[0] == self.__positions[1] and self.__positions[0] == self.__positions[2]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[0] == self.__positions[3] and self.__positions[0] == self.__positions[6]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[0] == self.__positions[4] and self.__positions[0] == self.__positions[8]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[6] == self.__positions[4] and self.__positions[6] == self.__positions[2]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[6] == self.__positions[7] and self.__positions[6] == self.__positions[8]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[1] == self.__positions[4] and self.__positions[1] == self.__positions[7]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[2] == self.__positions[5] and self.__positions[2] == self.__positions[8]:
#                 self.setGameState(False)
#                 winnerSign = "X"
#             elif self.__positions[0] == "X" and self.__positions[3] == self.__positions[4] and self.__positions[3] == self.__positions[5]:
#                 self.setGameState(False)
#                 winnerSign = "X"

#         finally:
#             if self.p1 == winnerSign:
#                 self.setWinner("Player One")
#             elif self.p2 == winnerSign:
#                 self.setWinner("Player Two")

#             return not self.getGameState()


#############################################################################################################################################

    # def positionAvailable(self, move):
    #     if self.__positions[move] == " ":
    #         return True

    #     return False

    # def winner(self, winner):
    #     x = self.getAllPosition().count("X")
    #     y = self.getAllPosition().count("y")

    #     if x > y:
    #         winner = "Player One"
    #         return True
    #     if y > x:
    #         winner = "Player Two"
    #         return True

    #     winner = "equalize"
    #     return False
