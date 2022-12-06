import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f'../input_files/input_{PROBLEM_NUM}.txt'

def solve(problem_num = "1"):
    with open(INPUT_PATH) as f:
        line = f.readline()
        num_unique_chars = 4 if problem_num == "1" else 14
        for i in range(num_unique_chars, len(line.strip())-1):
            substr = line[i-num_unique_chars:i]
            if len(set(substr)) == num_unique_chars:
                print(f"{substr=}, characters processed: {i}")
                break
            
if __name__ == '__main__':
    solve("1")
    solve("2")