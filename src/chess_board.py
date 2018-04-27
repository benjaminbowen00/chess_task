class ChessBoard:
    MAX_BOARD_WIDTH = 7
    MAX_BOARD_HEIGHT = 7

    def __init__(self):
        self.pieces = [[None] * 7 for _ in range(7)]

    def add(self, pawn, x_coordinate, y_coordinate, piece_color):
        pawn.x_coordinate = x_coordinate
        pawn.y_coordinate = y_coordinate
        pawn.piece_color = piece_color
        self.pieces[x_coordinate][y_coordinate] = pawn

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        raise NotImplementedError()
