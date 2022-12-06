from pathlib import Path
from collections import defaultdict
from copy import deepcopy

filename = "input.txt"
file = Path(filename)
file_gen = file.open()

#### parse header
is_header = True
stacks = defaultdict(list)
while is_header:
    line = next(file_gen)
    if not line.strip():
        is_header = False
        continue

    for i in range(len(line) // 4):
        element = line[i * 4 + 1]
        if not element.isalpha():
            continue
        else:
            stacks[i + 1].insert(0, element)

#### move stacks
stacks_new = deepcopy(stacks)
for line in file_gen:
    if not line.strip():
        continue

    num_blocks, from_, to_ = [int(x) for x in line.split() if x.isdigit()]

    #### part 1
    for _ in range(num_blocks):
        stacks[to_].append(stacks[from_].pop())

    #### part 2
    stacks_new[to_].extend(stacks_new[from_][-num_blocks:])
    [stacks_new[from_].pop() for _ in range(num_blocks)]

output1 = ""
output2 = ""
for k in sorted(stacks.keys()):
    output1 += stacks[k].pop()
    output2 += stacks_new[k].pop()

print("--- results ---")
print(f"{output1=}")
print(f"{output2=}")
