Comments
=======

## Getting the tests working:

if __name__ == '__main__':
    unittest.main()
Added to run the unittests.

import sys
sys.path.append("../")
Used sys.path.append to get the correct imports when running the tests from the tests directory.

__str__ changed to __unicode__ for use in python3

Extra test added to check pieces can't be put into a column with index 8.


## Comments about the game design:

Constants MAX_BOARD_WIDTH/HEIGHT changed to 8 so the list of lists of pieces produces 8 lists of length 8. Initializer uses the class variables, so they only need to be changed once for a different sized game.

Deleted chessboard from Pawn class - a chessboard has pieces, rather than a pawn has a chessboard.

At the moment the pawn controls moving itself, but this doesn't work when the move is a capture - as a check for a piece of the opposite colour is needed, or if it is a forward move but there is a piece in the way. Because of this I think it would work well to have an overall Game class that contains the board and the pieces. The Game class would have overall responsibility for making moves as it is necessary to check there is a piece of the opposite colour for a capture and check the move is legal.
The Game class would be responsible for the rules of the game: setting up the game, checking for checkmate, whose turn it is etc.
