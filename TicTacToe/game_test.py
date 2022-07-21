from game import Game

# Cell number greater than no. of cells Test Case
newGameOne = Game("Jim", "George")
def test_play_one():
    assert "Cell number out of board" == newGameOne.play(15)
    
# Cell Already Marked Test Case
newGameTwo = Game("Ravi", "Hari")
newGameTwo.board.cells[1].mark = "X"
def test_play_two():
    assert "Cell already marked" == newGameTwo.play(1)

# Draw Test Case
newGameThree = Game("Rahul", "Rishabh")
newGameThree.board.cells[1].mark = "X"
newGameThree.board.cells[0].mark = "O"
newGameThree.board.cells[3].mark = "X"
newGameThree.board.cells[2].mark = "O"
newGameThree.board.cells[4].mark = "X"
newGameThree.board.cells[5].mark = "O"
newGameThree.board.cells[6].mark = "X"
newGameThree.board.cells[7].mark = "O"
def test_play_three():
    assert "Draw" == newGameThree.play(8)

# Player wins Test Case
newGameFour = Game("Tom", "Jerry")
newGameFour.board.cells[1].mark = "X"
newGameFour.board.cells[3].mark = "O"
newGameFour.board.cells[2].mark = "X"
newGameFour.board.cells[4].mark = "O"
def test_play_four():
    assert "X" == newGameFour.play(0)

