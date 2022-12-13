import os
from functools import reduce
PROBLEM_NUM = int(''.join(filter(lambda i: i.isdigit(), os.path.basename(__file__).split('.')[0])))
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

def compare_lists(list_1, list_2):
    # zip the lists together and compare each element
    for i, j in zip(list_1, list_2):
        if isinstance(i, int) and isinstance(j, int):
            if i < j:
                return 1
            elif i > j:
                return -1
            else:
                continue

        elif isinstance(i, list) and isinstance(j, list):
            c = compare_lists(i, j)
            if c != 0:
                return c
                
        elif isinstance(i, int):
            c = compare_lists([i], j)
            if c != 0:
                return c
                
        elif isinstance(j, int):
            c = compare_lists(i, [j])
            if c != 0:
                return c

    if len(list_1) > len(list_2):
        return -1
    elif len(list_1) < len(list_2):
        return 1
    return 0

def solve_1():
    index_count = 0
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            packet_1 = eval(lines[i].strip())
            packet_2 = eval(lines[i+1].strip())
            true_order = compare_lists(packet_1, packet_2)
            
            print(f"Pair {i//3 + 1}:")
            print(f"Packet 1: {packet_1}")
            print(f"Packet 2: {packet_2}")
            print(f"Has correct order?: {true_order}\n")

            if true_order == 1:
                index_count += (i//3 + 1)


    print(f"Index sum: {index_count}")


def solve_2():
    packages = []
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == '':
                continue
            packages.append(eval(line.strip()))
        
    # append [[2]] and [[6]] to packages
    packages.append([[2]])
    packages.append([[6]])

    # sort packages using the compare_lists function
    from functools import cmp_to_key
    packages_sorted = sorted(packages, key=cmp_to_key(compare_lists), reverse=True)

    index1 = packages_sorted.index([[2]])+1
    index2 = packages_sorted.index([[6]])+1

    key = index1 * index2
    print(f"Key: {key}")    

if __name__ == '__main__':
    solve_1()
    solve_2()