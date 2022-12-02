import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f'../input_files/input_{PROBLEM_NUM}.txt'

def first():
    rps_lookup = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': 0,
        'Y': 1,
        'Z': 2,
    }
    total_score = 0
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            a, b = line.strip().split(' ')
            a, b = rps_lookup[a], rps_lookup[b]
            if a == b: # draw
                total_score += 3
            elif (a + 1) % 3 == b: # b wins
                total_score += 6
            else: # a wins
                total_score += 0

            total_score += (b + 1)

    print(f"{total_score=}")


def second():
    rps_lookup = {
        'A': 0,
        'B': 1,
        'C': 2,
    }
    total_score = 0
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            a, b = line.strip().split(' ')
            a = rps_lookup[a]
            if b == 'X': # loose
                total_score += 0
                my_choice = (a - 1) % 3
                total_score += my_choice + 1
            elif b == 'Y': # draw
                total_score += 3
                my_choice = a
                total_score += my_choice + 1
            else: # win
                total_score += 6
                my_choice = (a + 1) % 3
                total_score += my_choice + 1
            
    print(f"{total_score=}")

if __name__ == '__main__':
    # first()
    second()