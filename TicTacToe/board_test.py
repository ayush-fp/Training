from unittest import result
from board import Board
from cell import Cell

board = Board()
boardUnfinished = Board()

def test_one():
    board.cells[0].mark = "X" 
    board.cells[1].mark = "X"
    board.cells[2].mark = "X"

    # board.cells[3].mark = "X" 
    # board.cells[4].mark = "X"
    # board.cells[5].mark = "X"

    # board.cells[6].mark = "X" 
    # board.cells[7].mark = "X"
    # board.cells[8].mark = "X"

    # board.cells[0].mark = "X"
    # board.cells[3].mark = "X"
    # board.cells[6].mark = "X"

    # board.cells[1].mark = "X"
    # board.cells[4].mark = "X"
    # board.cells[7].mark = "X"

    # board.cells[2].mark = "X"
    # board.cells[5].mark = "X"
    # board.cells[8].mark = "X"

    # board.cells[0].mark = "X"
    # board.cells[4].mark = "X"
    # board.cells[8].mark = "X"

    # board.cells[2].mark = "X"
    # board.cells[4].mark = "X"
    # board.cells[6].mark = "X"

    win, symbol = board.resultAnalyser()
    if win == True:
        assert symbol == 'X'

def test_two():
    board.cells[0].mark = "O" 
    board.cells[1].mark = "O"
    board.cells[2].mark = "O"

    # board.cells[3].mark = "O" 
    # board.cells[4].mark = "O"
    # board.cells[5].mark = "O"

    # board.cells[6].mark = "O" 
    # board.cells[7].mark = "O"
    # board.cells[8].mark = "O"

    # board.cells[0].mark = "O"
    # board.cells[3].mark = "O"
    # board.cells[6].mark = "O"

    # board.cells[1].mark = "O"
    # board.cells[4].mark = "O"
    # board.cells[7].mark = "O"

    # board.cells[2].mark = "O"
    # board.cells[5].mark = "O"
    # board.cells[8].mark = "O"

    # board.cells[0].mark = "O"
    # board.cells[4].mark = "O"
    # board.cells[8].mark = "O"

    # board.cells[2].mark = "O"
    # board.cells[4].mark = "O"
    # board.cells[6].mark = "O"

    win, symbol = board.resultAnalyser()
    if win == True:
        assert symbol == 'O'

def test_three():
    board.cells[0].mark = "X"
    board.cells[1].mark = "X"
    board.cells[2].mark = "O"
    board.cells[3].mark = "O"
    board.cells[4].mark = "O"
    board.cells[5].mark = "X"
    board.cells[6].mark = "X"
    board.cells[7].mark = "O"
    board.cells[8].mark = "X"
    win, symbol = board.resultAnalyser()
    if win == False:
        assert symbol == 'Draw'

def test_four():
    boardUnfinished.cells[0].mark = 'X'
    boardUnfinished.cells[3].mark = 'O'
    win, symbol = boardUnfinished.resultAnalyser()
    if win == False:
        assert symbol == 'game unfinished'

