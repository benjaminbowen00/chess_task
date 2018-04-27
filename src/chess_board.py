class ChessBoard:
    MAX_BOARD_WIDTH = 7
    MAX_BOARD_HEIGHT = 7

    def __init__(self):
        self.pieces = [[None] * 7 for _ in range(7)]

    def add(self, pawn, x_coordinate, y_coordinate, piece_color):
        if self.pieces[y_coordinate][x_coordinate] is None:
            pawn.x_coordinate = x_coordinate
            pawn.y_coordinate = y_coordinate
            pawn.piece_color = piece_color
            self.pieces[y_coordinate][x_coordinate] = pawn
        else:
            pawn.x_coordinate = -1
            pawn.y_coordinate = -1
            pawn.piece_color = piece_color

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        is_legal_position = True
        if(x_coordinate > len(self.pieces[1]) or x_coordinate < 0):
            is_legal_position = False
        if(y_coordinate > len(self.pieces) or y_coordinate < 0):
            is_legal_position = False
        return is_legal_position
