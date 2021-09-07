import ctypes
import draughts
from math import ceil


def get_board(board):
    row = (ctypes.c_int * 8)
    checkerboard_board = (row * 8)()

    # From CheckerBoard API:
    WHITE = 1
    BLACK = 2
    MAN = 4
    KING = 8
    FREE = 0

    for loc in range(1, board.board.position_count + 1):
        piece = board.board.searcher.get_piece_by_position(loc)
        row = ceil(loc / board.board.width) - 1  # From get_row_from_position
        row = (board.board.height - 1) - row
        column = (loc - 1) % board.board.width  # From get_column
        if row % 2 == 0:
            column = (column + 1) * 2 - 2  # To account for the always empty white squares
        else:
            column = (column + 1) * 2 - 1  # To account for the always empty white squares
        number = FREE
        if piece:
            if piece.player == draughts.WHITE and not piece.king:
                number = BLACK + MAN
            elif piece.player == draughts.BLACK and not piece.king:
                number = WHITE + MAN
            elif piece.player == draughts.WHITE and piece.king:
                number = BLACK + KING
            elif piece.player == draughts.BLACK and piece.king:
                number = WHITE + KING
        checkerboard_board[column][row] = number

    return checkerboard_board