
from src.movement_type import MovementType
from src.piece_color import PieceColor

class Pawn:
    def __init__(self, piece_color):
        self._piece_color = piece_color
        self._chess_board = None
        self._x_coordinate = None
        self._y_coordinate = None

    @property
    def chess_board(self):
        return self._chess_board

    @chess_board.setter
    def chess_board(self, value):
        self._chess_board = value

    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, value):
        self._x_coordinate = value

    @property
    def y_coordinate(self):
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, value):
        self._y_coordinate = value

    @property
    def piece_color(self):
        return self._piece_color

    @piece_color.setter
    def piece_color(self, value):
        self._piece_color = value

    def move(self, movement_type, new_x, new_y):
        forward = 1
        if(self._piece_color == PieceColor.BLACK):
            forward = -1

        if(movement_type == MovementType.MOVE and new_x == self.x_coordinate and new_y == self.y_coordinate + forward):
            self.x_coordinate = new_x
            self.y_coordinate = new_y
        if(movement_type == MovementType.CAPTURE and new_x == (self.x_coordinate + 1 or self.x_coordinate - 1) and new_y == self.y_coordinate + forward):
            self.x_coordinate = new_x
            self.y_coordinate = new_y


    def __unicode__(self):
        return 'Current X: {}\nCurrent Y: {}\nPiece Color: {}'.format(
            self.x_coordinate, self.y_coordinate, self.piece_color
        )
