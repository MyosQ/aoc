import os
import inspect

def get_day_number(file: os.PathLike) -> int:
    digits = ''.join([c for c in os.path.basename(file) if c.isdigit()])
    if not digits:
        raise ValueError(f'No day number found in file name {os.path.basename(file)}')
    return int(digits)

def get_year(file: os.PathLike) -> int:
    year_dir = os.path.dirname(os.path.dirname(file))
    year = os.path.basename(year_dir)
    if not year.isdigit() and len(year) != 4:
        raise ValueError(f'No year found in dir name {year_dir}. Expected a 4 digit year as the dir name')
    return int(year)

def get_part_number(function_name: str) -> str:
    if function_name in ['first', 'part1', 'part_1', 'part_one', 'problem1', 'problem_1', 'problem_one']:
        return '1'
    elif function_name in ['second', 'part2', 'part_2', 'part_two', 'problem2', 'problem_2', 'problem_two']:
        return '2'
    else:
        return 'unknown'

def print_intro() -> None:
    frame_info = inspect.stack()[1]
    src_file = frame_info.filename
    src_function_name = frame_info.function
    part = get_part_number(src_function_name)
    day = get_day_number(src_file)
    year = get_year(src_file)
    print(f'\nAdvent of Code {year} - Day {day} (part {part})')

def get_input_file_path() -> os.PathLike:
    src_file = inspect.stack()[1].filename
    day_number = get_day_number(src_file)
    input_file = os.path.join(os.path.dirname(os.path.abspath(src_file)), '..', 'input_files', f'input{day_number}.txt')
    if not os.path.exists(input_file):
        raise FileNotFoundError(f'Input file for day {day_number} not found. Expected it to be at {input_file}')
    return input_file