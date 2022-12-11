import os
from functools import reduce
PROBLEM_NUM = int(''.join(filter(lambda i: i.isdigit(), os.path.basename(__file__).split('.')[0])))
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

monkeys = []

class Monkey:
    def __init__(self, index, items, operation, eval_func, divisor):
        self.index = index
        self.items = items
        self.operation = operation
        self.eval_func = eval_func
        self.divisor = divisor
        self.num_inspections = 0
    
    def __repr__(self):
        return f"Monkey({self.index}, {self.items}, {self.operation}, {self.eval_func})"

    def catch(self, item):
        self.items.append(item)
        return

    def turn(self, problem_num, mgm):
        while len(self.items) > 0:
            item = self.items.pop(0)
            worry_level = self.operation(item)
            if problem_num == "1":
                worry_level //= 3
            elif problem_num == "2":
                worry_level %= mgm
            throw_to_index = self.eval_func(worry_level)
            monkeys[throw_to_index].catch(worry_level)
            self.num_inspections += 1
        return

def solve(problem_num = "1"):
    global monkeys
    monkeys = []
    with open(INPUT_PATH) as f:
        f = [line for line in f.readlines() if not line == '\n']
        monkey_index = 0
        lines_per_monkey = 6
        for i in range(0, len(f), lines_per_monkey):
            chunk = f[i:i+lines_per_monkey]
            items = [int(i) for i in chunk[1].strip().split('Starting items: ')[1].split(',')]
            operation = eval(chunk[2].strip().split('Operation: ')[1].replace('new = ', 'lambda old: '))
            test_func_divisible_by = int(chunk[3].strip().split('Test: ')[1].split(' ')[-1])
            if_true = int(chunk[4].strip().split('If true: ')[1].split(' ')[-1])
            if_false = int(chunk[5].strip().split('If false: ')[1].split(' ')[-1])
            test_func = lambda x, mod=test_func_divisible_by, t=if_true, f=if_false: t if x % mod == 0 else f
            monkeys.append(Monkey(monkey_index, items, operation, test_func, test_func_divisible_by))
            monkey_index += 1
            
    rounds = 20 if problem_num == "1" else 10_000
    mgm = reduce((lambda x, y: x * y), [monkey.divisor for monkey in monkeys]) # smallest common multiple
    for i in range(1, rounds+1):
        for monkey in monkeys:
            monkey.turn(problem_num, mgm)

    # get the two monkeys with the most inspections
    max_two_inspection = sorted([monkey.num_inspections for monkey in monkeys])[-2:]    
    monkey_business = max_two_inspection[0] * max_two_inspection[1]
    print(f"Problem {problem_num}: {monkey_business=}")
    
if __name__ == '__main__':
    solve("1")
    solve("2")