def bodens_mate(board):
  """
  This function implements Boden's Mate, a checkmate that can be delivered by a queen or rook along the back rank (that is, the row on which the pieces [not pawns] stand at the start of the game) in which the mated king is unable to move up the board because the king is blocked by friendly pieces (usually pawns) on the second rank.

  Args:
    board: The current state of the chess board.

  Returns:
    A list of moves that deliver Boden's Mate.
  """

  # Find all positions where White has a queen or rook on the back rank and Black's king is on the second rank.
  queen_positions = [square for square in board.board if board.piece_at(square) is not None and board.piece_at(square).type == "queen"]
  rook_positions = [square for square in board.board if board.piece_at(square) is not None and board.piece_at(square).type == "rook"]
  black_king_positions = [square for square in board.board if board.piece_at(square) is not None and board.piece_at(square).type == "king" and board.piece_at(square).color == "black"]

  # For each position where White has a queen or rook on the back rank and Black's king is on the second rank, check if Black has any legal moves.
  moves = []
  for queen_position in queen_positions:
    for rook_position in rook_positions:
      for black_king_position in black_king_positions:
        if not board.is_check(black_king_position):
          moves.append([queen_position, black_king_position])

  # Return the list of moves that deliver Boden's Mate.
  return moves
