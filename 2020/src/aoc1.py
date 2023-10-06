import itertools
from utils import get_input_file_path, print_intro

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        numbers = [int(line) for line in f.readlines()]

    for a, b in itertools.combinations(numbers, 2):
        if a + b == 2020:
            print(f'Found a + b = 2020. a = {a}, b = {b}. a * b = {a * b}')
            break

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        numbers = [int(line) for line in f.readlines()]

    for a, b, c in itertools.combinations(numbers, 3):
        if a + b + c == 2020:
            print(f'Found a + b + c = 2020. a = {a}, b = {b}, c = {c}. a * b * c = {a * b * c}')
            break

if __name__ == '__main__':
    first()
    second()
