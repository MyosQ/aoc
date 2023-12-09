from utils import get_input_file_path, print_intro

def parse_input(f: str) -> list[list[int]]:
    return [[int(i) for i in line.split()] for line in f]

def get_diff_seq(seq: list[int]) -> list[int]:
    return [seq[i+1] - seq[i] for i in range(len(seq) - 1)]

def get_next_value(seq: list[int]) -> int:
    next_val = seq[-1]
    while True:
        seq = get_diff_seq(seq)
        if set(seq) == {0}:
            return next_val
        next_val += seq[-1]

def get_prev_value(seq: list[int]) -> int:
    prev_val = seq[0]
    i = 1
    while True:
        seq = get_diff_seq(seq)
        if set(seq) == {0}:
            return prev_val

        prev_val += seq[0] if i % 2 == 0 else -seq[0]
        i += 1

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        sequences = parse_input(f)
        next_val_sum = 0
        for seq in sequences:
            next_val_sum += get_next_value(seq)

    print(next_val_sum)

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        sequences = parse_input(f)
        prev_val_sum = 0
        for seq in sequences:
            prev_val_sum += get_prev_value(seq)

    print(prev_val_sum)

if __name__ == '__main__':
    first()
    second()
