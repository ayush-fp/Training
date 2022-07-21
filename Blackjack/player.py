class Player:
    def __init__(self, name) -> None:
        self.points = 0
        self.skipUsed = False
        self.name = name
    
    def skip(self):
        if self.skipUsed == False:
            self.skipUsed = True
            return True, "Move Skipped"
        else:
            return False, "Already Skipped Once, Pick a card"