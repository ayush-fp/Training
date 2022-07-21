from board import Board
from cell import Cell
from player import Player


newPlayer = Player("Jim", "X")
boardOne = Board()
boardOne.cells[3].mark = "O"
cellNumOne = 3

boardTwo = Board()
cellNumTwo = 1

def test_mark_one():
    isCellMarked, message = newPlayer.markCell(boardOne.cells[cellNumOne])
    assert isCellMarked == False

def test_mark_two():
    isCellMarked, message = newPlayer.markCell(boardTwo.cells[cellNumTwo])
    assert isCellMarked == True