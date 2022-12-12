import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

class RopeLink:
    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
        self.prev = None

    def __repr__(self) -> str:
        return f"RopeLink({self.pos}, {self.name})"
    
    def move(self, pos):
        self.pos = pos

    def dir(self, other):
        return (self.pos[0] - other.pos[0], self.pos[1] - other.pos[1])


class Rope:
    def __init__(self, start_pos):
        self.head = RopeLink(start_pos, "H")

    def __repr__(self) -> str:
        margin = 5
        (min_x, max_x), (min_y, max_y) = self.__get_bounding_box()
        square_size_x = max_x - min_x + 2 * margin
        square_size_y = max_y - min_y + 2 * margin
        shift_x = -min_x + margin
        shift_y = -min_y + margin
        grid = [["." for _ in range(square_size_y)] for _ in range(square_size_x)]
        margin = 5
        link = self.head
        while link:
            if grid[link.pos[0] + shift_x][link.pos[1] + shift_y] == ".":
                grid[link.pos[0] + shift_x][link.pos[1] + shift_y] = link.name
            link = link.prev

        grid_str = ""
        for row in grid[::-1]:
            grid_str += "".join(row)
            grid_str += "\n"
        return grid_str

    def __get_bounding_box(self):
        link = self.head
        min_x, max_x = link.pos[0], link.pos[0]
        min_y, max_y = link.pos[1], link.pos[1]
        while link.prev:
            link = link.prev
            min_x = min(min_x, link.pos[0])
            max_x = max(max_x, link.pos[0])
            min_y = min(min_y, link.pos[1])
            max_y = max(max_y, link.pos[1])
        return (min_x, max_x), (min_y, max_y)

    def append_link(self, name, parent=None):
        parent = self.get_tail() if parent is None else parent
        new_link = RopeLink(parent.pos, name)
        parent.prev = new_link
        return new_link

    def get_tail(self):
        link = self.head
        while link.prev:
            link = link.prev
        return link

    def update(self):
        link = self.head
        while link.prev:
            prev_link = link.prev
            dir = link.dir(prev_link)
            if abs(dir[0]) == 2 and abs(dir[1]) == 2:
                prev_link.move((link.pos[0] - dir[0] // 2, link.pos[1] - dir[1] // 2))
            else:
                if dir[0] == 2:
                    prev_link.move((link.pos[0] - 1, link.pos[1]))
                elif dir[0] == -2:
                    prev_link.move((link.pos[0] + 1, link.pos[1]))
                
                if dir[1] == 2:
                    prev_link.move((link.pos[0], link.pos[1] - 1))
                elif dir[1] == -2:
                    prev_link.move((link.pos[0], link.pos[1] + 1))
            link = link.prev

def solve(problem_num = "1"):

    rope = Rope((0, 0))
    if problem_num == "1":
        rope.append_link("T")
    elif problem_num == "2":
        rope.append_link("1")
        rope.append_link("2")
        rope.append_link("3")
        rope.append_link("4")
        rope.append_link("5")
        rope.append_link("6")
        rope.append_link("7")
        rope.append_link("8")
        rope.append_link("9")

    all_tail_pos = set()
    with open(INPUT_PATH) as f:
        for line in f.readlines():
            dir, dist = line.strip().split(' ')
            if dir == 'R':
                move_to = lambda pos: (pos[0], pos[1] + 1)
            elif dir == 'L':
                move_to = lambda pos: (pos[0], pos[1] - 1)
            elif dir == 'U':
                move_to = lambda pos: (pos[0] + 1, pos[1])
            elif dir == 'D':
                move_to = lambda pos: (pos[0] - 1, pos[1])
            for _ in range(int(dist)):
                head = rope.head
                head.move(move_to(head.pos))
                rope.update()
                tail = rope.get_tail()
                all_tail_pos.add(tail.pos)

    print(f"Problem {problem_num}")
    print(f"End position: \n{rope}")
    print(f"Unique tail positions: {len(all_tail_pos)}\n\n")

if __name__ == '__main__':
    solve("1")
    solve("2")