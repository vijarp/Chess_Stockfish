from stockfish import Stockfish

# Initialize Stockfish with the path to the Stockfish executable
path = "stockfish.exe"
stockfish = Stockfish(path=path)

# Set the position using a list of moves from the starting position
stockfish.set_position(["e2e4", "e7e5", "g1f3", "b8c6"])

# Get the best move
best_move = stockfish.get_best_move()
print("Next best move:", best_move)