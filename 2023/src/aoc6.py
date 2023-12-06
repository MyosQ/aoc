from utils import get_input_file_path, print_intro

def parse_input(f):
    # E.g:
    # Time:      7  15   30
    # Distance:  9  40  200
    times = ' '.join(f.readline().split(":")[1].split()).split(" ")
    distances = ' '.join(f.readline().split(":")[1].split()).split(" ")
    return [int(t) for t in times], [int(d) for d in distances]

def parse_input2(f):
    times = int(''.join(f.readline().split(":")[1].split()))
    distances = int(''.join(f.readline().split(":")[1].split()))
    return times, distances

def get_num_of_possible_wins(t, d):
    return sum([1 for i in range(t+1) if i*(t-i) > d])

def first():
    print_intro()
    wins_product = 1
    with open(get_input_file_path(), "r") as f:
        times, distances = parse_input(f)
        for t, d in zip(times, distances):
            wins_product *= get_num_of_possible_wins(t, d)

    print(wins_product)

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        t, d = parse_input2(f)
        print(get_num_of_possible_wins(t, d))

if __name__ == '__main__':
    first()
    second()
