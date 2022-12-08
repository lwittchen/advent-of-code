from collections import deque

filename = "input.txt"
message = open(filename).read().strip()

def parse_message(message: str, maxlen: int) -> int:
    queue = deque(maxlen=maxlen)
    for i, char in enumerate(message):
        queue.append(char)
        if len(set(queue)) == maxlen:
            return i + 1
    raise BaseException("No Start Position Found!")

result = parse_message(message, maxlen=4)
result2 = parse_message(message, maxlen=14)

print('--- results ---')
print(f'{result=}')
print(f'{result2=}')