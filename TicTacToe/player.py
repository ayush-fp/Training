class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def markCell(self, cell):
        if cell.isMarked():
            return False, "Cell already marked"
        else:
            cell.mark = self.symbol
            return True, "Cell marked by the player"