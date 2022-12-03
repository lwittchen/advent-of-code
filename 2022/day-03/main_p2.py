from pathlib import Path
from string import ascii_letters
    
def process_badge(lines: str) -> int: 
    """split line and find common char """
    assert len(lines) == 3, 'not three lines'

    common = set(lines[0]) & set(lines[1]) & set(lines[2])
    assert len(common) == 1, "More than one common char!"

    return ascii_letters.index(common.pop())

def group_by_three(iterator): 
    output = []
    for i, x in enumerate(iterator, start=1):
        output.append(x.strip())
        if (i % 3) == 0:
            yield output 
            output.clear()

if __name__ == "__main__":
    file_name = "input.txt"
    file = Path(file_name)

    total_prio = 0
    for lines in group_by_three(file.open()):
        print(lines)
        prio = process_badge(lines)
        total_prio += prio + 1
    
    print('--- result ---')
    print(f'--- total prio: {total_prio}')