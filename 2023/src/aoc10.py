from utils import get_input_file_path, print_intro

PIPE_DIRECTIONS = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}

def is_valid_direction(direction: tuple[int, int], next_cell: str) -> bool:
    return (-direction[0], -direction[1]) in PIPE_DIRECTIONS[next_cell]

def parse_into_grid(f: str) -> list[list[str]]:
    return [list(line.strip()) for line in f.readlines()]

def get_start_pos(grid: list[list[str]]) -> tuple[int, int]:
    return next((i, j) for i, line in enumerate(grid) for j, char in enumerate(line) if char == "S")

def get_start_directions(grid: list[list[str]], start_pos: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    dirs = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if dx * dy != 0:
                continue
            if grid[start_pos[0] + dx][start_pos[1] + dy] != "." and \
                is_valid_direction((dx, dy), grid[start_pos[0] + dx][start_pos[1] + dy]):
                dirs.append((dx, dy))

    return dirs
            
def next_pos_direction(grid: list[list[str]], pos: tuple[int, int], direction: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    x, y = pos
    dx, dy = direction
    new_pos = (x + dx, y + dy)
    new_cell = grid[new_pos[0]][new_pos[1]]

    if new_cell == "S":
        return new_pos, None

    for new_direction in PIPE_DIRECTIONS[new_cell]:
        if new_direction != (-dx, -dy):
            return new_pos, new_direction

def find_loop(start_pos: tuple[int, int], grid: list[list[str]]) -> list[tuple[int, int]]:
    visited = set()
    pos1 = pos2 = start_pos
    start_direction1, start_direction2 = get_start_directions(grid, start_pos)
    next_direction1 , next_direction2 = start_direction1, start_direction2
    distances = {}
    step = 0

    while True:
        if pos1 in visited and pos1 != start_pos:
            return distances
        visited.add(pos1)
        distances[pos1] = step
        pos1, next_direction1 = next_pos_direction(grid, pos1, next_direction1)

        if pos2 in visited and pos2 != start_pos:
            return distances
        visited.add(pos2)
        distances[pos2] = step
        pos2, next_direction2 = next_pos_direction(grid, pos2, next_direction2)

        step += 1
    

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        grid = parse_into_grid(f)
        start_pos = get_start_pos(grid)
        loop_distances = find_loop(start_pos, grid)
        print(max(loop_distances.values()))

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
