from unittest import skip
from deck import Deck
from player import Player


class Game:
    def __init__(self, playerOneName, playerTwoName):
        self.playerOne = Player(playerOneName)
        self.playerTwo = Player(playerTwoName)
        self.deck = Deck.createDeck()
        self.turn = 1
    
    def play(self):
    
        if self.turn%2 == 1:
            player = self.playerOne
        else:
            player = self.playerTwo
        
        if self.playerOne.skipUsed == True and self.playerTwo.skipUsed == True:
            if self.playerOne.points == self.playerTwo.points:
                print("Draw")
                return "Draw"
            elif self.playerOne.points > self.playerTwo.points:
                print(f'{self.playerOne.name} Wins!')
                return f'{self.playerOne.name} Wins!'
            else:
                print(f'{self.playerTwo.name} Wins!')
                return f'{self.playerTwo.name} Wins!'

        else:      
            choice = str(input(f"{player.name} : pick or skip"))
            if choice == 'skip':
                isSkip, skipMessage = player.skip()
                if isSkip:
                    print(skipMessage)
                    self.turn = self.turn + 1
                    return skipMessage
                else:
                    print(skipMessage)
                    return skipMessage
            else:
                player.points = player.points + self.deck.pickCardFromDeck()
                if player.points == 21:
                    print(f'{player.name} Wins!')
                    return f'{player.name} Wins!'
                if player.points > 21:
                    print(f'{player.name} lost')
                    return f'{player.name} lost'