from utils import get_input_file_path, print_intro
from queue import PriorityQueue

# 2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533

def parse_input(f):
    return [[{
        "cost": int(c),
        "min_accumulated_cost": 0,
        "min_cost_prev": None,
        "visited": False
    } for c in line.strip()] for line in f]
    

def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        dp = parse_input(f)

        q = PriorityQueue()
        q.put((0, 0))

        while not q.empty():
            # pop current position
            x, y = q.get()

            # check if we've visited this position before
            if dp[x][y]["visited"]:
                continue

            # get current cost
            current_cost = dp[x][y]["cost"]

            # get neighbors
            neighbors = []
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(dp[0]) or ny >= len(dp):
                    continue
                neighbors.append((nx, ny))

            if len([n for n in neighbors if dp[n[0]][n[1]]["visited"]]) == 0: # No neighbors visited. Top left corner.
                dp[x][y]["min_accumulated_cost"] = current_cost
                dp[x][y]["min_cost_prev"] = None
            else:
                dp[x][y]["min_accumulated_cost"] = min([dp[n[0]][n[1]]["min_accumulated_cost"] for n in neighbors if dp[n[0]][n[1]]["visited"]]) + current_cost
                dp[x][y]["min_cost_prev"] = min([n for n in neighbors if dp[n[0]][n[1]]["visited"]], key=lambda n: dp[n[0]][n[1]]["min_accumulated_cost"])

            dp[x][y]["visited"] = True

            # add neighbors to queue
            for nx, ny in neighbors:
                if not dp[nx][ny]["visited"] and (nx, ny) not in q.queue:
                    q.put((nx, ny))

            print("Visited:", (x, y))
            print(dp[x][y])

    # print traceback
    x, y = len(dp[0]) - 1, len(dp) - 1
    while dp[x][y]["min_cost_prev"] is not None:
        print((x, y))
        x, y = dp[x][y]["min_cost_prev"]

    print("Min cost:", dp[len(dp) - 1][len(dp[0]) - 1]["min_accumulated_cost"])


def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        ...

if __name__ == '__main__':
    first()
    # second()
