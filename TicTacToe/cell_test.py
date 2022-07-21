import pytest
from cell import Cell

newCell = Cell()

def test_one():
    flag = newCell.isMarked()
    assert flag == False

def test_two():
    newCell.mark = "X"
    flag = newCell.isMarked()
    assert flag == True

def test_three():
    newCell.mark = "O"
    flag = newCell.isMarked()
    assert flag == True

def test_four():
    newCell.mark = "arbitary"
    flag = newCell.isMarked()
    assert flag == False