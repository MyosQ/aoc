import os
PROBLEM_NUM = int(''.join(filter(lambda i: i.isdigit(), os.path.basename(__file__).split('.')[0])))
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

def solve_1():
    x_register = 1
    cycle = 0
    total_signal_strength = 0
    with open(INPUT_PATH) as f:
        for line in f.readlines():
            line = line.strip()
            if line == 'noop':
                num_cycles = 1
                arg = 0
            elif line.startswith('addx'):
                num_cycles = 2
                arg = int(line.split(' ')[1])
            
            for _ in range(num_cycles):
                cycle += 1
                if cycle >= 20 and (cycle-20) % 40 == 0:
                    total_signal_strength += x_register*cycle

            x_register += arg
    print(f"Problem 1: {total_signal_strength=}")

def solve_2():
    grid_width, grid_height = 40, 6
    grid = [['.' for _ in range(grid_width)] for _ in range(grid_height)]
    sprite_position = 1
    cycle = 0
    with open(INPUT_PATH) as f:
        for line in f.readlines():
            line = line.strip()
            if line == 'noop':
                num_cycles = 1
                arg = 0
            elif line.startswith('addx'):
                num_cycles = 2
                arg = int(line.split(' ')[1])
            for _ in range(num_cycles):
                cycle += 1
                grid_position = ((cycle-1) // grid_width, (cycle-1) % grid_width)
                if abs(sprite_position - grid_position[1]) <= 1:
                    grid[grid_position[0]][grid_position[1]] = '#'
                    
            sprite_position += arg
    
    print("Problem 2:")
    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    solve_1()
    solve_2()