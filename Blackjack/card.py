class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.inDeck = True
    
    @staticmethod
    def createCard(suit, value):
        return Card(suit, value)