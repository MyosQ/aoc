import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

def solve():
    grid = []
    with open(INPUT_PATH) as f:
        for line in f.readlines():
            line = line.strip()
            row = []
            [row.append(int(c)) for c in line]
            grid.append(row)

    tot_visible = 2*len(grid) + 2*len(grid[0]) - 4 # edges
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):

            val = grid[i][j]
            # check if any cell to the right is larger than current cell
            for k in range(j + 1, len(grid[0])):
                if grid[i][k] >= val:
                    break
            else:
                tot_visible += 1
                continue

            # check if any cell to the left is larger than current cell
            for k in range(j - 1, -1, -1):
                if grid[i][k] >= val:
                    break
            else:
                tot_visible += 1
                continue
            
            # check if any cell above is larger than current cell
            for k in range(i - 1, -1, -1):
                if grid[k][j] >= val:
                    break
            else:
                tot_visible += 1
                continue
            
            # check if any cell below is larger than current cell
            for k in range(i + 1, len(grid)):
                if grid[k][j] >= val:
                    break
            else:
                tot_visible += 1
                continue

    print(f"Part 1: {tot_visible}")

    max_scenic_score = 1
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):

            scenic_score = 1
            val = grid[i][j]

            # check if any cell to the right is larger than current cell
            for k in range(j + 1, len(grid[0])):
                if grid[i][k] >= val:
                    break
            scenic_score *= (k - j)

            # check if any cell to the left is larger than current cell
            for k in range(j - 1, -1, -1):
                if grid[i][k] >= val:
                    break
            scenic_score *= (j - k)
            
            # check if any cell above is larger than current cell
            for k in range(i - 1, -1, -1):
                if grid[k][j] >= val:
                    break
            scenic_score *= (i - k)
            
            # check if any cell below is larger than current cell
            for k in range(i + 1, len(grid)):
                if grid[k][j] >= val:
                    break
            scenic_score *= (k - i)

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    
    print(f"Part 2: {max_scenic_score}")
    return

if __name__ == '__main__':
    solve()