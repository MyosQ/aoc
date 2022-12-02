import numpy as np
def first():
    max_sum, sum = 0, 0
    with open('../input_files/input_1.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                if sum > max_sum:
                    max_sum = sum
                sum = 0
                continue
            sum += int(line)
    
    print(f"{max_sum=}")

def second():
    sum = 0
    top_three_sorted = [0, 0, 0]
    with open('../input_files/input_1.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                if sum > top_three_sorted[0]:
                    top_three_sorted[0] = sum
                    top_three_sorted.sort()
                sum = 0
                continue
            sum += int(line)
    
    print(f"{top_three_sorted=}")
    print(f"top three sum: {np.sum(top_three_sorted)}")

if __name__ == '__main__':
    # first()
    second()