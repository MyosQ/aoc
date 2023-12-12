from utils import get_input_file_path, print_intro

def parse_input(f: str) -> tuple[list[int], list[dict]]:
    seed_line = f.readline().split('seeds: ')[1]
    seeds = [int(seed) for seed in seed_line.split()]
    f.readline()
    sections = f.read().split('\n\n')
    maps = []

    for section in sections:
        map = {}
        lines = section.split('\n')
        map['from'], map['to'] = lines[0].split(' ')[0].split('-to-')

        ranges = []
        for line in lines[1:]:
            ranges.append(tuple(int(x) for x in line.split(' ')))

        map['ranges'] = ranges
        maps.append(map)

    return seeds, maps
    
def map_number(number: int, ranges: list[tuple[int, int, int]]) -> int:
    for range in ranges:
        dest_range_start, source_range_start, range_len = range[0], range[1], range[2]
        if number >= source_range_start and number < source_range_start + range_len:
            return dest_range_start + number - source_range_start

    return number

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        seeds, maps = parse_input(f)

        min_location_num = 1e9
        for seed_number in seeds:
            from_category = "seed"
            number = seed_number
            while from_category != "location":
                for map in maps:
                    if map['from'] == from_category:
                        to_category = map['to']
                        ranges = map['ranges']
                        break
                else:
                    raise Exception(f"no map from {from_category}")

                from_category = to_category
                number = map_number(number, ranges)

            location_num = number
            if location_num < min_location_num:
                min_location_num = location_num

        print(f"Closes location: {min_location_num}")

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
