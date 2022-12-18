import os
from functools import reduce
PROBLEM_NUM = int(''.join(filter(lambda i: i.isdigit(), os.path.basename(__file__).split('.')[0])))
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

def getTotalSurfaceArea(cubes: set):
    total_surface_area = 0
    for cube in cubes:
        x, y, z = cube
        num_neighbors = 0
        for d in [-1, 1]:
            if (x + d, y, z) in cubes:
                num_neighbors += 1
            if (x, y + d, z) in cubes:
                num_neighbors += 1
            if (x, y, z + d) in cubes:
                num_neighbors += 1

        total_surface_area += 6 - num_neighbors
    return total_surface_area


def solve_1():
    cubes = set()
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            x, y, z = line.strip().split(',')
            cubes.add((int(x), int(y), int(z)))

    print("Problem 1:")
    print(f"Total surface area: {getTotalSurfaceArea(cubes)}")

def solve_2():
    cubes = set()
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            x, y, z = line.strip().split(',')
            cubes.add((int(x), int(y), int(z)))

    #  get the min and max coords
    max_x = max([x for x, _, _ in cubes])
    max_y = max([y for _, y, _ in cubes])
    max_z = max([z for _, _, z in cubes])
    
    # create grid of zeros from 0 to max_dim + margin
    margin = 1
    grid = [[[0 for _ in range(max_z + margin + 1)] for _ in range(max_y + margin + 1)] for _ in range(max_x + margin + 1)]

    #  populate grid with air/droplets represented by 1s
    # start at 0,0,0 and go to max_x, max_y, max_z
    # using djikstra's algorithm
    # set the start point to 1 and add 1 to all neighbors that are not in cubes
    #  repeat until no more 1s are added
    grid[0][0][0] = 1
    change_made = True
    while change_made:
        change_made = False
        for x in range(max_x + margin + 1):
            for y in range(max_y + margin + 1):
                for z in range(max_z + margin + 1):
                    if (x, y, z) in cubes or grid[x][y][z] == 1:
                        continue
                    if x-1 >= 0:
                        if grid[x-1][y][z] == 1:
                            grid[x][y][z] = 1
                            change_made = True
                    if y-1 >= 0:
                        if grid[x][y-1][z] == 1:
                            grid[x][y][z] = 1
                            change_made = True
                    if z-1 >= 0:
                        if grid[x][y][z-1] == 1:
                            grid[x][y][z] = 1
                            change_made = True
                    if x+1 <= max_x + margin:
                        if grid[x+1][y][z] == 1:
                            grid[x][y][z] = 1
                            change_made = True
                    if y+1 <= max_y + margin:
                        if grid[x][y+1][z] == 1:
                            grid[x][y][z] = 1
                            change_made = True
                    if z+1 <= max_z + margin:
                        if grid[x][y][z+1] == 1:
                            grid[x][y][z] = 1
                            change_made = True


    cubes_no_air_pockets = set()
    for x in range(max_x + margin + 1):
        for y in range(max_y + margin + 1):
            for z in range(max_z + margin + 1):
                if grid[x][y][z] == 0:
                    cubes_no_air_pockets.add((x, y, z))
    
    print("Problem 2:")
    print(f"Total surface area: {getTotalSurfaceArea(cubes_no_air_pockets)}")

if __name__ == '__main__':
    solve_1()
    solve_2()