from cell import Cell


class Board:
    def __init__(self) -> None:
        self.cells = [Cell() for cell in range(9)]
    
    def isBoardFull(self):
        for cell in self.cells:
            if cell.isMarked():
                continue
            else:
                return False
        return True

    def resultAnalyser(self):

        if self.cells[0].mark == "X" and self.cells[1].mark == "X" and self.cells[2].mark == "X":
            return True, "X"
        if self.cells[3].mark == "X" and self.cells[4].mark == "X" and self.cells[5].mark == "X":
            return True, "X"
        if self.cells[6].mark == "X" and self.cells[7].mark == "X" and self.cells[8].mark == "X":
            return True, "X"
        if self.cells[0].mark == "X" and self.cells[3].mark == "X" and self.cells[6].mark == "X":
            return True, "X"
        if self.cells[1].mark == "X" and self.cells[4].mark == "X" and self.cells[7].mark == "X":
            return True, "X"
        if self.cells[2].mark == "X" and self.cells[5].mark == "X" and self.cells[8].mark == "X":
            return True, "X"
        if self.cells[0].mark == "X" and self.cells[4].mark == "X" and self.cells[8].mark == "X":
            return True, "X"
        if self.cells[2].mark == "X" and self.cells[4].mark == "X" and self.cells[6].mark == "X":
            return True, "X"
        
        if self.cells[0].mark == "O" and self.cells[1].mark == "O" and self.cells[2].mark == "O":
            return True, "O"
        if self.cells[3].mark == "O" and self.cells[4].mark == "O" and self.cells[5].mark == "O":
            return True, "O"
        if self.cells[6].mark == "O" and self.cells[7].mark == "O" and self.cells[8].mark == "O":
            return True, "O"
        if self.cells[0].mark == "O" and self.cells[3].mark == "O" and self.cells[6].mark == "O":
            return True, "O"
        if self.cells[1].mark == "O" and self.cells[4].mark == "O" and self.cells[7].mark == "O":
            return True, "O"
        if self.cells[2].mark == "O" and self.cells[5].mark == "O" and self.cells[8].mark == "O":
            return True, "O"
        if self.cells[0].mark == "O" and self.cells[4].mark == "O" and self.cells[8].mark == "O":
            return True, "O"
        if self.cells[2].mark == "O" and self.cells[4].mark == "O" and self.cells[6].mark == "O":
            return True, "O"
        
        else:
            isFull = self.isBoardFull()
            if isFull:
                return False, "Draw"
            else:
                return False, "game unfinished"
    
    def printBoard(self):
        i = 0
        for c in self.cells:
            i = i + 1
            print(c.mark, end=" ")
            if i == 3 or i == 6:
                print('\n')