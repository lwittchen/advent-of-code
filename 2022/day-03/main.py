from pathlib import Path
from string import ascii_letters
    
def process_line(line: str) -> int: 
    """split line and find common char """

    split = len(line) // 2
    first_part = set(line[:split]) 
    second_part = set(line[split:])

    common = first_part & second_part
    assert len(common) == 1, "More than one common char!"

    return ascii_letters.index(common.pop())

if __name__ == "__main__":
    file_name = "input.txt"
    file = Path(file_name)

    total_prio = 0
    for line in file.open():
        prio = process_line(line.strip())
        total_prio += prio + 1
    
    print('--- result ---')
    print(f'--- total prio: {total_prio}')


