from utils import get_input_file_path, print_intro

def first_digit(line):
    for c in line:
        if c in "0123456789":
            return c
    return None

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        print(sum(int(first_digit(line) + first_digit(line[::-1])) for line in f.readlines()))

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        sum = 0
        for line in f.readlines():
            line = (
                line
                .replace("one", "o1e")
                .replace("two", "t2o")
                .replace("three", "t3e")
                .replace("four", "f4r")
                .replace("five", "f5e")
                .replace("six", "s6x")
                .replace("seven", "s7n")
                .replace("eight", "e8t")
                .replace("nine", "n9e")
            )
            sum += int(first_digit(line) + first_digit(line[::-1]))

    print(sum)

if __name__ == '__main__':
    first()
    second()
