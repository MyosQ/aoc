from utils import get_input_file_path, print_intro

def parse_games(data: str) -> dict:
    games = {}
    for line in data.strip().split('\n'):
        parts = line.split(':')
        game_id = int(parts[0].split(' ')[1])
        draws = parts[1].split(';')
        draws_parsed = []
        for draw in draws:
            cubes = draw.strip().split(', ')
            draw_dict = {'red': 0, 'green': 0, 'blue': 0}
            for cube in cubes:
                count, color = cube.split(' ')
                draw_dict[color] = int(count)
            draws_parsed.append(draw_dict)
        games[game_id] = draws_parsed
    return games

def is_possible(draws: list[dict], bag_contents: dict) -> bool:
    for draw in draws:
        for color, count in draw.items():
            if count > bag_contents[color]:
                return False
    return True

def get_minimum_set(draws: list[dict]) -> dict:
    minimum_set = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        for color, count in draw.items():
            if count > minimum_set[color]:
                minimum_set[color] = count
    return minimum_set

def first():
    print_intro()
    bag_contents = {'red': 12, 'green': 13, 'blue': 14}
    sum_possible_ids = 0

    with open(get_input_file_path(), "r") as f:
        games = parse_games(f.read())
    
    for game_id, draws in games.items():
        sum_possible_ids += game_id if is_possible(draws, bag_contents) else 0

    print(f'Sum of possible game ids: {sum_possible_ids}')

def second():
    print_intro()
    sum_of_powers = 0

    with open(get_input_file_path(), "r") as f:
        games = parse_games(f.read())
    
    for _, draws in games.items():
        min_set = get_minimum_set(draws)
        sum_of_powers += min_set['red'] * min_set['green'] * min_set['blue']

    print(f'Sum of powers: {sum_of_powers}')

if __name__ == '__main__':
    first()
    second()
