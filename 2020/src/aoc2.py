from utils import get_input_file_path, print_intro

def is_valid1(line):
    min_max, letter_colon, pwd = line.split(' ')
    min, max = min_max.split('-')
    letter = letter_colon[0]
    count = pwd.count(letter)
    return int(min) <= count <= int(max)

def is_valid2(line):
    positions, letter_colon, pwd = line.split(' ')
    pos1, pos2 = positions.split('-')
    letter = letter_colon[0]
    return (pwd[int(pos1)-1] == letter) != (pwd[int(pos2)-1] == letter)

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        sum_valid = 0
        for line in f.readlines():
            if is_valid1(line):
                sum_valid += 1
        print(sum_valid)

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        sum_valid = 0
        for line in f.readlines():
            if is_valid2(line):
                sum_valid += 1
        print(sum_valid)

if __name__ == '__main__':
    first()
    second()