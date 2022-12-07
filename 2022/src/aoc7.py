import os
PROBLEM_NUM = os.path.basename(__file__).split('.')[0][-1]
INPUT_PATH = f"../input_files/input_{PROBLEM_NUM}.txt"

class Tree:
    def __init__(self, name, parent = None, is_leaf = False, size = None):
        self.children = []
        self.node_name = name
        self.is_leaf = is_leaf
        self.size = size
        self.parent = parent
    
    def __repr__(self):
        return f"{self.node_name} ({self.size})"
    
    def add_child(self, child):
        assert isinstance(child, Tree)
        child.parent = self
        self.children.append(child)


def solve(problem_num = "1"):
    
    pwd_stack = []
    t = Tree("/")
    current_tree = t

    with open(INPUT_PATH) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("$"): # command
                command = line.replace("$ ", "")
                if command.startswith("ls"):
                    continue
                elif command.startswith("cd"):
                    ch_dir = command.split(" ")[1]
                    if ch_dir == "..":
                        pwd_stack.pop()
                        new_dir = pwd_stack[-1]
                        current_tree = current_tree.parent

                    else:
                        pwd_stack.append(ch_dir)
                        new_dir = ch_dir
                        for child in current_tree.children:
                                if child.node_name == new_dir:
                                    current_tree = child

            else: # result from "ls"
                name = line.split(" ")[1]
                if line.startswith("dir"): #directory
                    current_tree.add_child(Tree(name))
                else: #file
                    size = int(line.split(" ")[0])
                    current_tree.add_child(Tree(name, is_leaf = True, size = size))    
    
    # update the size of directory node
    def update_sizes(t):
        if t.is_leaf:
            return t.size
        else:
            t.size = sum([update_sizes(child) for child in t.children])
            return t.size
    update_sizes(t)

    if problem_num == "1":
        # find all the directories that have a size smaller than 100_000 and sum their sizes
        def find_small_dirs(t):
            if t.size < 100_000 and not t.is_leaf:
                global size_sum
                size_sum += t.size
            for child in t.children:
                find_small_dirs(child)
        find_small_dirs(t)
        print(f"Problem 1: {size_sum=}")

    elif problem_num == "2":
        def get_size_used(t):
            if t.is_leaf:
                return t.size
            else:
                return sum([get_size_used(child) for child in t.children])
        
        def find_smallest_to_delete(t):
            global smallest_sofar
            if t.size > delete_at_least and not t.is_leaf and t.size < smallest_sofar:
                smallest_sofar = t.size
            for child in t.children:
                find_smallest_to_delete(child)
        
        size_used = get_size_used(t)
        delete_at_least = size_used - 40_000_000
        find_smallest_to_delete(t)
        print(f"Problem 2: {smallest_sofar=}")

# global variables
size_sum: int = 0
smallest_sofar: int = 100_000_000

if __name__ == '__main__':
    solve("1")
    solve("2") 