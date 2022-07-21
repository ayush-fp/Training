import random
from card import Card


class Deck:
    def __inint__(self, listOfCards):
        self.deck = listOfCards

    @staticmethod
    def createDeck():
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        listOfCards = []
        for suit in suits:
            for value in range(1,14):
                if value == 1:
                    card = Card.createCard(suit, 'ace')
                elif value == 11:
                    card = Card.createCard(suit, 'jack')
                elif value == 12:
                    card = Card.createCard(suit, 'queen')
                elif value == 13:
                    card = Card.createCard(suit, 'king')
                else:
                    card = Card.createCard(suit, str(value))
                listOfCards.append(card)
        random.shuffle(listOfCards)
        return Deck(listOfCards)

    @staticmethod
    def askPlayer():
        point = int(input("You got an ace, input point 1 or 11"))
        return point

    def pickCardFromDeck(self):
        point = 0
        for card in self.deck:
            if card.inDeck == True:
                if card.value == 'king' or card.value == 'queen' or card.value == 'jack':
                    point = 10
                elif card.value == 'ace':
                    point = Deck.askPlayer()
                else:
                    point = int(card.value)
                card.inDeck = False
                return point