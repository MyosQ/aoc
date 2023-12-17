from utils import get_input_file_path, print_intro
import numpy as np
from hashlib import sha256

def parse_input(f):
    return np.array([list(line.strip()) for line in f])        

def tilt_north(grid):
    rolling_rock_set = set()
    for i in range(1, grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == "O":
                rolling_rock_set.add((i, j))

    while len(rolling_rock_set) > 0:
        i, j = rolling_rock_set.pop()
        for k in range(i - 1, -1, -1):
            if grid[k, j] == ".":
                grid[k, j] = "O"
                grid[i, j] = "."
                rolling_rock_set.add((k, j))
                break
            elif grid[k, j] == "#":
                break

    return grid

def tilt_cycle(grid):
    grid = tilt_north(grid) # tilt north
    grid = np.rot90(grid, k=-1)
    grid = tilt_north(grid) # tilt west
    grid = np.rot90(grid, k=-1)
    grid = tilt_north(grid) # tilt south
    grid = np.rot90(grid, k=-1)
    grid = tilt_north(grid) # tilt east
    grid = np.rot90(grid, k=-1)
    return grid, sha256(grid.tobytes()).hexdigest()

def get_total_load(grid):
    total_load = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == "O":
                total_load += grid.shape[0] - i

    return total_load

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        print("Total load:", get_total_load(tilt_north(parse_input(f))))

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        grid = parse_input(f)
        num_cycles = 1_000_000_000

        cycles = [{
            "hash": sha256(grid.tobytes()).hexdigest(),
            "load": get_total_load(grid)
        }]

        for i in range(num_cycles):
            grid, grid_hash = tilt_cycle(grid)
            
            if grid_hash in [c["hash"] for c in cycles]:
                cycle_start = [i for i, c in enumerate(cycles) if c["hash"] == grid_hash][0]
                cycle_length = i + 1 - cycle_start
                break

            cycles.append({
                "hash": grid_hash,
                "load": get_total_load(grid)
            })

        corresponding_cycle = (num_cycles - cycle_start) % cycle_length
        load = cycles[cycle_start + corresponding_cycle]["load"]
        print(f"Total load after {num_cycles:,} cycles:", load)

if __name__ == '__main__':
    first()
    second()

