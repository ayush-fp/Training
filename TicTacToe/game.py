from pytest import mark
from board import Board
from player import Player


class Game:
    def __init__(self, playerOneName, playerTwoName):
        self.playerOne = Player(playerOneName, "X")
        self.playerTwo = Player(playerTwoName, "O")
        self.board = Board()
        self.turn = 1
    
    def play(self, cellNum):

                
        if self.turn%2 == 1:
            player = self.playerOne
        else:
            player = self.playerTwo

        if cellNum > 8 or cellNum < 0:
            print("Cell number out of board")
            return "Cell number out of board"

        isCellMarked, markMessage = player.markCell(self.board.cells[cellNum])
        if isCellMarked == True:
            checkResultAgain, analyserMessage = self.board.resultAnalyser()
            if checkResultAgain == True:
                print("Winner is: ", analyserMessage)
                return analyserMessage
            elif checkResultAgain == False and analyserMessage == "Draw":
                print("Game Draw")
                return analyserMessage
            elif checkResultAgain == False and analyserMessage == "game unfinished":
                self.turn = self.turn + 1
                print(markMessage)
                return markMessage

        else:
            print(markMessage)
            return markMessage
            

if __name__ == "__main__":
    newGame = Game("Jim", "George")
    print(newGame.playerOne.name, ": ", newGame.playerOne.symbol)
    print(newGame.playerTwo.name, ": ", newGame.playerTwo.symbol)
    # X win moves:
    newGame.play(1)
    newGame.play(3)
    newGame.play(2)
    newGame.play(4)
    newGame.play(0)
    
    # Game draw moves:
    # newGame.play(1)
    # newGame.play(0)
    # newGame.play(3)
    # newGame.play(2)
    # newGame.play(4)
    # newGame.play(5)
    # newGame.play(6)
    # newGame.play(7)
    # newGame.play(8)