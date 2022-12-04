import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f'../input_files/input_{PROBLEM_NUM}.txt'

def solve(problem = "two"):
    count = 0
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            pairs_lims = line.strip().split(',')

            lims0 = [int(n) for n in pairs_lims[0].split('-')]
            sections0 = set(range(lims0[0], lims0[1]+1))

            lims1 = [int(n) for n in pairs_lims[1].split('-')]
            sections1 = set(range(lims1[0], lims1[1]+1))
            
            
            if problem == "one": # if one is subset of the other
                if sections0.issubset(sections1) or sections1.issubset(sections0):
                    count += 1
            elif problem == "two": # if they intersect
                if sections0.intersection(sections1):
                    count += 1

    print(count)

if __name__ == '__main__':
    solve("one")
    solve("two")