from utils import get_input_file_path, print_intro

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
