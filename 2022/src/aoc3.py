import os
from itertools import islice

PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f'../input_files/input_{PROBLEM_NUM}.txt'

def first():
    priority_sum = 0
    with open(INPUT_PATH) as f:
        for line in f.readlines():
            line, half_len = line.strip(), len(line.strip())//2
            comp1 = set(line[:half_len])
            comp2 = set(line[half_len:])
            item = comp1.intersection(comp2).pop()

            if ord(item) < 91:
                priority_sum += ord(item) - 64 + 26 # A-Z
            elif ord(item) > 96:
                priority_sum += ord(item) - 96 # a-z

    print(f"{priority_sum=}")           
    return


def second():
    priority_sum = 0
    with open(INPUT_PATH) as f:
        while True:
            three_lines = islice(f, 3)
            sets = [set(line.strip()) for line in three_lines]
            if sets == []:
                break
            item = sets[0].intersection(sets[1], sets[2]).pop()

            if ord(item) < 91:
                priority_sum += ord(item) - 64 + 26 # A-Z
            elif ord(item) > 96:
                priority_sum += ord(item) - 96 # a-z            
            
    print(f"{priority_sum=}")           
    return

if __name__ == '__main__':
    # first()
    second()