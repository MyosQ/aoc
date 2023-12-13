from utils import get_input_file_path, print_intro

def parse_input(f: str) -> list:
    grids, grid = [], []
    for line in f:
        if line == "\n":
            grids.append(grid)
            grid = []
            continue
        grid.append([c for c in line.strip()])
    grids.append(grid)

    return grids

def get_reflections(grid: list) -> tuple[int, str]:
    """ Position and type of reflections"""

    # Check for horizontal reflection between r and r+1
    num_rows = len(grid)
    for r in range(num_rows-1):
        is_reflection = True
        i = 0
        while r - i >= 0 and r + i + 1 < num_rows:
            if grid[r-i] != grid[r+i+1]:
                is_reflection = False
                break
            i += 1 

        if is_reflection:
            return (r+1, "horizontal")
        
    # Check for vertical reflection between c and c+1
    num_cols = len(grid[0])
    for c in range(num_cols-1):
        is_reflection = True
        i = 0
        while c - i >= 0 and c + i + 1 < num_cols:
            if [row[c-i] for row in grid] != [row[c+i+1] for row in grid]:
                is_reflection = False
                break
            i += 1 

        if is_reflection:
            return (c+1, "vertical")

    return (-1, "none")

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        grids = parse_input(f)
        sum_reflections = 0
        for grid in grids:
            reflection = get_reflections(grid)
            if reflection[1] == "horizontal":
                sum_reflections += reflection[0]*100
            elif reflection[1] == "vertical":
                sum_reflections += reflection[0]
            else:
                raise Exception("No valid reflection found")

        print(f"Sum of reflections: {sum_reflections}")

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
