# Author: Diego Vallejo

import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    
    if len(opponent_history) > 1:
        last_move = opponent_history[-1]
        if last_move == "R":
            return "P"
        elif last_move == "P":
            return "S"
        elif last_move == "S":
            return "R"
    
    return random.choice(["R", "P", "S"])
