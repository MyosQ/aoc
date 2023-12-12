from utils import get_input_file_path, print_intro
import itertools

def parse_input(f: str) -> list[list[str]]:
    return [list(line.strip()) for line in f.readlines()]

def get_galaxy_dist(g1: tuple[int, int], g2: tuple[int, int], empty_rows_indices: list[int], empty_cols_indices: list[int]) -> int:
    
    # x distance
    min_x, max_x = min(g1[0], g2[0]), max(g1[0], g2[0])
    x_dist = max_x - min_x
    for i in range(min_x, max_x):
        if i in empty_rows_indices:
            x_dist += 1_000_000 - 1 # 1 if part 1

    # y distance
    min_y, max_y = min(g1[1], g2[1]), max(g1[1], g2[1])
    y_dist = max_y - min_y
    for i in range(min_y, max_y):
        if i in empty_cols_indices:
            y_dist += 1_000_000 - 1 # 1 if part 1

    return x_dist + y_dist


def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        grid = parse_input(f)
        num_rows, num_cols = len(grid), len(grid[0])
        empty_rows_indices = [i for i, row in enumerate(grid) if all([c == '.' for c in row])]
        empty_cols_indices = [i for i, col in enumerate(zip(*grid)) if all([c == '.' for c in col])]
        galaxies = [(r, c) for r in range(num_rows) for c in range(num_cols) if grid[r][c] == '#']
        
        dist_sum = 0
        for g1, g2 in itertools.combinations(galaxies, 2):
            dist = get_galaxy_dist(g1, g2, empty_rows_indices, empty_cols_indices)
            dist_sum += dist

        print(dist_sum)

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
