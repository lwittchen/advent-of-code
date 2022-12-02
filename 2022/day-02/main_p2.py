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
        
win_map = {
    Move.PAPER: Move.SCISSOR,
    Move.SCISSOR: Move.ROCK,
    Move.ROCK: Move.PAPER
}
lose_map = {
    Move.PAPER: Move.ROCK,
    Move.SCISSOR: Move.PAPER,
    Move.ROCK: Move.SCISSOR
}
result_map = {
    "X": Result.LOSE,
    "Y": Result.DRAW,
    "Z": Result.WIN
}
def match_outcome(outcome: Result, elve_move: Move):
    if outcome == Result.DRAW:
        return elve_move
    elif outcome == Result.WIN:
        return win_map[elve_move]
    elif outcome == Result.LOSE: 
        return lose_map[elve_move]

def play_game(elve: str, outcome: str) -> int:
    elve_move = parse_move(elve)
    match_result = result_map[outcome]
    own_move = match_outcome(match_result, elve_move)
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
