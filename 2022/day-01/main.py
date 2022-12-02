from pathlib import Path

class ScoreBoard:
    def __init__(self):
        self.scores = [0, 0, 0]

    def insert(self, new_score):
        new_scores = self.scores + [new_score]
        self.scores = sorted(new_scores)[1:]
        return None

    @property
    def total_score(self):
        return sum(self.scores)

    @property
    def top_score(self):
        return self.scores[2]


if __name__ == "__main__":
    filename = "input.txt"
    file = Path(filename)

    max_cal = 0
    curr_cal = 0
    score_board = ScoreBoard()
    for line in file.open():
        if line.strip():
            curr_cal += int(line)
            continue

        score_board.insert(curr_cal)
        curr_cal = 0
        
    # include last score - last line has no newline char
    score_board.insert(curr_cal)

    print("--- Results ---")
    print(f"Max Cal: {score_board.top_score}")
    print(f"Total Cal: {score_board.total_score}")
