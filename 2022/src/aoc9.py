import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"
# INPUT_PATH = f"../input_files/samp.txt"

def solve_1():
    with open(INPUT_PATH) as f:
        head_pos = [0, 0]
        tail_rel_pos = [0, 0] # x, y
        all_tail_pos = set()
        all_tail_pos.add((0, 0))

        for line in f.readlines():
            dir, dist = line.strip().split(' ')            
            if dir == 'R':
                for _ in range(int(dist)):
                    head_pos[1] += 1
                    if tail_rel_pos[1] == 0 or tail_rel_pos[1] == 1:
                        tail_rel_pos[1] -= 1
                    else:
                        tail_rel_pos = [0, -1]
                    tail_pos = (head_pos[0] + tail_rel_pos[0], head_pos[1] + tail_rel_pos[1])
                    all_tail_pos.add(tail_pos)
                    
            elif dir == 'L':
                for _ in range(int(dist)):
                    head_pos[1] -= 1
                    if tail_rel_pos[1] == 0 or tail_rel_pos[1] == -1:
                        tail_rel_pos[1] += 1
                    else:
                        tail_rel_pos = [0, 1]
                    tail_pos = (head_pos[0] + tail_rel_pos[0], head_pos[1] + tail_rel_pos[1])
                    all_tail_pos.add(tail_pos)

            elif dir == 'U':
                for _ in range(int(dist)):
                    head_pos[0] += 1
                    if tail_rel_pos[0] == 0 or tail_rel_pos[0] == 1:
                        tail_rel_pos[0] -= 1
                    else:
                        tail_rel_pos = [-1, 0]
                    tail_pos = (head_pos[0] + tail_rel_pos[0], head_pos[1] + tail_rel_pos[1])
                    all_tail_pos.add(tail_pos)
            
            elif dir == 'D':
                for _ in range(int(dist)):
                    head_pos[0] -= 1
                    if tail_rel_pos[0] == 0 or tail_rel_pos[0] == -1:
                        tail_rel_pos[0] += 1
                    else:
                        tail_rel_pos = [1, 0]
                    tail_pos = (head_pos[0] + tail_rel_pos[0], head_pos[1] + tail_rel_pos[1])
                    all_tail_pos.add(tail_pos)

    print(len(all_tail_pos))
    return

class RopeLink:
    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"RopeLink({self.pos}, {self.name})"

class Rope:
    def __init__(self, start_pos):
        self.head = RopeLink(start_pos, "H")

    def __repr__(self) -> str:
        s = f"Rope({self.head})"
        prev = self.head.prev
        while prev:
            s += f" -> {prev}"
            prev = prev.prev
        return s

    def append_link(self, pos, name, parent):
        # assert parent is RopeLink
        assert parent.pos == pos
        new_link = RopeLink(pos, name)
        new_link.next = parent
        parent.prev = new_link
        return new_link
        



def solve_2():

    rope = Rope((0, 0))
    rl = rope.append_link((0, 0), "1", rope.head)
    rl = rope.append_link((0, 0), "2", rl)
    rl = rope.append_link((0, 0), "3", rl)
    rl = rope.append_link((0, 0), "4", rl)
    rl = rope.append_link((0, 0), "5", rl)
    print(f"{rope}")

    with open(INPUT_PATH) as f:
        pass

if __name__ == '__main__':
    # solve_1()
    solve_2()