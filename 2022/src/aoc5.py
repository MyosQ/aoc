import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f'../input_files/input_{PROBLEM_NUM}.txt'

def solve(problem_num = "1"):
    with open(INPUT_PATH) as f:
        lines = f.readlines()
        spaces_per_symbol = 4
        num_stacks = int(len(lines[0])/spaces_per_symbol)
        stacks = [[]*num_stacks for _ in range(num_stacks)]

        def read_initial_structure():
            while True:
                line = lines.pop(0).strip('\n')

                if line == "":
                    break

                if not '[' in line or not ']' in line:
                    continue
                line = line.replace(' '*spaces_per_symbol, '\t').replace('[', '').replace(']', '').replace(' ', '')

                for i, el in enumerate(line):
                    if not el == '\t':
                        stacks[i].append(el.strip('[]'))

            # Reverse the stacks to get them in the correct order
            for i in range(len(stacks)):
                stacks[i] = stacks[i][::-1]          
        
            return

        def perform_moves(problem_num = "1"):
            while lines:
                line = lines.pop(0)
                digits = [int(s) for s in line.split() if s.isdigit()]
                amount_to_move = digits[0]
                from_stack_index = digits[1]-1
                to_stack_index = digits[2]-1

                if problem_num == "1":
                    for _ in range(amount_to_move):
                        stacks[to_stack_index].append(stacks[from_stack_index].pop())
                elif problem_num == "2":
                    stacks[to_stack_index] += stacks[from_stack_index][-amount_to_move:]
                    stacks[from_stack_index] = stacks[from_stack_index][:-amount_to_move]

            return
            
        read_initial_structure()
        perform_moves(problem_num)
        print(''.join([s[-1] for s in stacks]))
            
if __name__ == '__main__':
    solve("1")
    solve("2")