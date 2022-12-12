import os
from functools import reduce
PROBLEM_NUM = int(''.join(filter(lambda i: i.isdigit(), os.path.basename(__file__).split('.')[0])))
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

class Node: 
    def __init__(self, name, min_path=None):
        self.name = name
        self.min_path = min_path
    
    def __repr__(self):
        return f"{self.name}"

def min_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def solve(problem_num="1"):
    grid = []
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            row = []
            for c in line:
                if c == 'S':
                    row.append(Node('a', 0))
                elif problem_num == "2" and c == 'a':
                    row.append(Node('a', 0))
                elif c == 'E':
                    row.append(Node('z'))
                    end_pos = (len(grid), len(row)-1)
                else:
                    row.append(Node(c))
            grid.append(row)

    # loop through grid and find min path to each node using Dijkstra's algorithm.
    updated = True
    while updated:
        updated = False
        for i in range(len(grid)):
            for j in range(0, len(grid[0])):
                # get min path to this node
                current_min_path = grid[i][j].min_path
                min_path = current_min_path
                name = grid[i][j].name
                # check cell to the left
                if j > 0 and grid[i][j-1].min_path is not None and ord(grid[i][j-1].name) - ord(name) >= -1:
                    min_path = min_none(min_path, grid[i][j-1].min_path + 1)
                # check cell above
                if i > 0 and grid[i-1][j].min_path is not None and ord(grid[i-1][j].name) - ord(name) >= -1:
                    min_path = min_none(min_path, grid[i-1][j].min_path + 1)
                # check cell below
                if i < len(grid)-1 and grid[i+1][j].min_path is not None and ord(grid[i+1][j].name) - ord(name) >= -1:
                    min_path = min_none(min_path, grid[i+1][j].min_path + 1)
                # check cell to the right
                if j < len(grid[0])-1 and grid[i][j+1].min_path is not None and ord(grid[i][j+1].name) - ord(name) >= -1:
                    min_path = min_none(min_path, grid[i][j+1].min_path + 1)

                if min_path and (current_min_path is None or current_min_path > min_path):
                    grid[i][j].min_path = min_path
                    updated = True
            
    print(grid[end_pos[0]][end_pos[1]].min_path)

if __name__ == '__main__':
    solve("1")
    solve("2")