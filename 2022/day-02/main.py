from pathlib import Path
from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

def parse_move(input: str) -> Move: 
    if input in ['A', 'X']: 
        return Move.ROCK
    elif input in ['B', 'Y']: 
        return Move.PAPER
    elif input in ['C', 'Z']:
        return Move.SCISSOR
    else:
        raise NotImplementedError
        
def match_moves(own_move: Move, elve_move: Move):
    if own_move == elve_move:
        return Result.DRAW
    elif any(
        [
            (own_move == Move.SCISSOR) and (elve_move == Move.PAPER),
            (own_move == Move.PAPER) and (elve_move == Move.ROCK),
            (own_move == Move.ROCK) and (elve_move == Move.SCISSOR),
        ]
    ):
        return Result.WIN
    else:
        return Result.LOSE

def play_game(elve: str, own: str) -> int:
    own_move = parse_move(own)
    elve_move = parse_move(elve)
    match_result = match_moves(own_move, elve_move)
    return match_result.value + own_move.value

if __name__ == "__main__":

    filename = "input.txt"
    file = Path(filename)

    outcomes = list()
    for line in file.open():
        elve, own = line.strip().split()
        outcome = play_game(elve, own)
        outcomes.append(outcome)
    
    print('--- Result ---')
    print(f'Total sum: {sum(outcomes)}')
