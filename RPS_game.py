# Author: Diego Vallejo

import random

def play(player1, player2, num_games, verbose=False):
    player1_wins = 0
    player2_wins = 0
    ties = 0

    for _ in range(num_games):
        p1_move = player1("")
        p2_move = player2("")

        if p1_move == p2_move:
            ties += 1
        elif (p1_move == "R" and p2_move == "S") or (p1_move == "P" and p2_move == "R") or (p1_move == "S" and p2_move == "P"):
            player1_wins += 1
        else:
            player2_wins += 1
        
        if verbose:
            print(f"Player 1: {p1_move}, Player 2: {p2_move}")

    print(f"Player 1 wins: {player1_wins}")
    print(f"Player 2 wins: {player2_wins}")
    print(f"Ties: {ties}")

def quincy(prev_play):
    return random.choice(["R", "P", "S"])

def johnny(prev_play):
    return "R"

def jake(prev_play):
    return "P"

def jane(prev_play):
    return "S"
