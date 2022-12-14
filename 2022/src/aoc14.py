import os
from functools import reduce
PROBLEM_NUM = int(''.join(filter(lambda i: i.isdigit(), os.path.basename(__file__).split('.')[0])))
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

def getBounds():
    x_min, x_max, y_max = -1, -1, -1
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            coords = line.strip().split(' -> ')
            for coord in coords:
                x, y = coord.split(',')
                x, y = int(x), int(y)
                if x < x_min or x_min == -1:
                    x_min = x
                if x > x_max or x_max == -1:
                    x_max = x
                if y > y_max or y_max == -1:
                    y_max = y
    return x_min, x_max, 0, y_max

def fill_with_rocks(grid, shift):
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            coords = line.strip().split(' -> ')
            prev_x, prev_y = None, None
            for coord in coords:
                x, y = coord.split(',')
                x, y = int(x), int(y)
                if prev_x is not None:
                    if prev_x == x:
                        start = prev_y if prev_y < y else y
                        end = prev_y if prev_y > y else y
                        for i in range(start, end+1):
                            grid[x+shift][i] = '#'
                    else:
                        start = prev_x if prev_x < x else x
                        end = prev_x if prev_x > x else x
                        for i in range(start, end+1):
                            grid[i+shift][y] = '#'
                prev_x, prev_y = x, y

def print_grid_and_count(grid, sand_count):
    grid_transpose  = list(map(list, zip(*grid)))
    for row in grid_transpose:
        print(''.join(row))

    print(f"Sand count: {sand_count}")


def solve(problem_num="1"):
    sand_source = (500, 0)
    x_min, x_max, y_min, y_max = getBounds()
    x_margin = y_max+2
    y_margin = 3
    grid = [['.' for _ in range(y_min, y_max+1+y_margin)] for _ in range(x_min-x_margin, x_max+1+x_margin)]
    shift = -x_min+x_margin
    grid[sand_source[0]+shift][sand_source[1]] = '+'
    fill_with_rocks(grid, shift)

    # floor
    if problem_num == "2":
        for i in range(x_min-x_margin, x_max+1+x_margin):
            grid[i+shift][y_max+2] = '#'

    sand_count = 0
    reached_source, reached_max = False, False
    while not reached_source and not reached_max :
        sand_pos = sand_source
        to_rest = False
        while not to_rest:
            if sand_pos[1] > y_max+2:
                reached_max = True
                break

            pos_below = grid[sand_pos[0]+shift][sand_pos[1]+1]
            pos_below_left = grid[sand_pos[0]+shift-1][sand_pos[1]+1]
            pos_below_right = grid[sand_pos[0]+shift+1][sand_pos[1]+1]
            
            if pos_below == '#' or pos_below == 'o':
                if pos_below_left == '.':
                    sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
                elif pos_below_right == '.':
                    sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
                else:
                    grid[sand_pos[0]+shift][sand_pos[1]] = 'o'
                    sand_count += 1
                    to_rest = True
                    if sand_pos == sand_source:
                        reached_source = True
                        break
                    
            elif pos_below == '.':
                sand_pos = (sand_pos[0], sand_pos[1]+1)

    print_grid_and_count(grid, sand_count)

if __name__ == '__main__':
    solve("1")
    solve("2")
