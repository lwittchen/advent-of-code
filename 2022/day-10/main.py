from pathlib import Path 

filename = 'input.txt'
lines = [line.strip() for line in Path(filename).open() if line.strip()]

x = 1
shifts = []
for line in lines:
    if line.startswith('noop'):
        curr_shift = 0 
        shifts.append(x)
    else:
        _, curr_shift = line.split()
        shifts.extend([x]*2)
    
    x += int(curr_shift)

results = 0
for cycle, x in enumerate(shifts, start=1):
    if (cycle > 0) and (cycle + 20) % 40 == 0:
        print(cycle, x)
        results += x * cycle

print('--- results ---')
print(f'{results=}')
