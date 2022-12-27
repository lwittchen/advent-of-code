from dataclasses import dataclass
from functools import partial, reduce

op_map = {
    "+": lambda a, b: a+b,
    "*": lambda a, b: a * b, 
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b,
}

@dataclass
class Monkey:
    id_: int
    items: list 
    operation: callable 
    test: callable
    throw_true: int
    throw_false: int

    def __post_init__(self):
        self.counter = 0

    def do_operation(self, value: int):
        return self.operation(value)

    def do_test(self, value: int):
        return self.test(value)

    def add_item(self, item: int):
        self.items.append(item)

    def throw(self, item):
        recipient = self.throw_true if self.do_test(item) else self.throw_false
        return recipient, item

    def run_round(self):
        results = list()
        for item in self.items: 
            self.counter += 1
            out = self.do_operation(item)
            out = out // 3
            results.append(self.throw(out))
        self.items = list()
        return results

def parse_operation(x, first, second, op_func):
    return op_func(x if first == "old" else int(first), x if second == "old" else int(second))

def parse_test(x, test_num):
    return (x % test_num) == 0

if __name__ == "__main__":

    filename = 'input.txt'
    lines = [line.strip() for line in open(filename) if line.strip()]

    monkey_params = dict()
    monkeys = dict()
    for line in lines: 
        if line.startswith('Monkey'):
            if monkey_params:
                monkeys[monkey_params['id_']] = Monkey(**monkey_params)
                monkey_params.clear()

            monkey_params['id_'] = int(line.split()[-1][:-1])

        if line.startswith('Starting'):
            items = list(map(int, line.split(':')[1].split(',')))
            monkey_params['items'] = items 

        if line.startswith('Operation'):
            first, op, second = line.split('=')[1].split()
            op_func = op_map[op]
            operation = partial(parse_operation, first=first, second=second, op_func=op_func) 
            monkey_params['operation'] = operation
                
        if line.startswith('Test'):
            test_num =  int(line.split()[-1])
            monkey_params['test'] = partial(parse_test, test_num=test_num)

        if line.startswith('If true'):
            monkey_params['throw_true'] = int(line.split()[-1])

        if line.startswith('If false'):
            monkey_params['throw_false'] = int(line.split()[-1])
            
monkeys[monkey_params['id_']] = Monkey(**monkey_params)

for _ in range(20):
    for _, monkey in monkeys.items():
        pairs = monkey.run_round()
        for id_, item in pairs:
            monkeys[id_].add_item(item)

counters = [monkey.counter for monkey in monkeys.values()]
result = reduce(lambda a, b: a*b, sorted(counters)[-2:])

breakpoint()
print('--- results ---')
print(f"{result=}")
