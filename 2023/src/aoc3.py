from utils import get_input_file_path, print_intro


def parse_input(f):
    return [line.strip() for line in f.readlines()]

def has_symbol(schematic, x, y):
    non_symbols = set(".1234567890")
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= x+dx < len(schematic[0]) and 0 <= y+dy < len(schematic):
                if schematic[y+dy][x+dx] not in non_symbols:
                    return True 
    return False

def sum_part_numbers(schematic):
    total_sum = 0
    current_number = ""
    num_has_symbol = False

    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if char.isdigit():
                current_number += char
                if has_symbol(schematic, x, y):
                    num_has_symbol = True
                
                if x == len(row) - 1 or not row[x + 1].isdigit():    
                    if num_has_symbol:
                        total_sum += int(current_number)

                    current_number = ""
                    num_has_symbol = False
            else:
                current_number = ""
                num_has_symbol = False
    return total_sum

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        schematic = parse_input(f)

    print(f"Sum of part numbers: {sum_part_numbers(schematic)}")
    

def has_gear_symbol(schematic, x, y) -> (bool, (int, int)):
    gear_symbol = set("*")
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= x+dx < len(schematic[0]) and 0 <= y+dy < len(schematic):
                if schematic[y+dy][x+dx] in gear_symbol:
                    return True, f"{x+dx}, {y+dy}"
    return False, None

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        schematic = parse_input(f)

    gears = {}
    current_number = ""
    gear_symbol = False
    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if char.isdigit():
                current_number += char
                t, p = has_gear_symbol(schematic, x, y)
                if t:
                    gear_symbol = True
                    pos = p
                if x == len(row) - 1 or not row[x + 1].isdigit():    
                    if gear_symbol:
                        if pos not in gears:
                            gears[pos] = []
                        gears[pos] += [int(current_number)]
                    current_number = ""
                    gear_symbol = False

            else:
                current_number = ""
                gear_symbol = False
    
    product_sum = 0
    for pos, numbers in gears.items():
        if len(numbers) == 2:
            product_sum += numbers[0] * numbers[1]

    print(f"Sum of gear ratios: {product_sum}")


if __name__ == '__main__':
    first()
    second()
