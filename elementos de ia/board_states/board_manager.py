import numpy as np
import os

def save_board_state(board, level):
    """Saves each move with spacing in a clean format"""
    os.makedirs("board_states", exist_ok=True)
    filename = f"board_states/level_{level}_game.txt"
    
    with open(filename, 'a') as f:  # 'a' = append mode
        # Save board with newlines between rows
        np.savetxt(f, board, fmt='%d')
        f.write("\n")  # Extra newline between moves
    
    return filename

def load_board_states(level):
    """Loads all moves with proper formatting"""
    filename = f"board_states/level_{level}_game.txt"
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r') as f:
        content = f.read().strip().split("\n\n")  # Split by double newline
    
    moves = []
    for move in content:
        moves.append(np.loadtxt(move.splitlines(), dtype=int))
    
    return moves