if __name__ == '__main__':
    unittest.main()
in test files

import sys
sys.path.append("../")
to get correct imports

Problem with MAX_BOARD_WIDTH/HEIGHT being 7 (due to list index)

decided best to change max_width to 8

Deleted chessboard from pawn class - a chessboard has pieces, rather than a pawn has a chessboard

__str__ to __unicode__ in python 3
