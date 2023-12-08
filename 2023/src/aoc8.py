from utils import get_input_file_path, print_intro

def parse_input(f: str) -> (str, dict):
    instructions = f.readline().strip()
    f.readline() # Skip the empty line
    node_map = {}
    for line in f:
        node, children_str = line.strip().split(' = ')
        node_map[node] = tuple(children_str[1:-1].split(', '))
    return instructions, node_map

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.label} -> ({self.left.label}, {self.right.label})"
    
    def __str__(self):
        return f"{self.label} -> ({self.left.label}, {self.right.label})"

def build_directed_graph(node_map: dict) -> list[Node]:
    nodes = {}
    for node_label, children_labels in node_map.items():
        node = nodes.get(node_label, Node(node_label))
        nodes[node_label] = node

        left_label, right_label = children_labels
        node.left = nodes.get(left_label, Node(left_label))
        nodes[left_label] = node.left

        node.right = nodes.get(right_label, Node(right_label))
        nodes[right_label] = node.right

    return nodes

def count_steps_to_node(instructions: str, start_node: Node, end_node: Node) -> int:
    node = start_node
    num_steps = 0
    while True:
        for c in instructions:
            if c == 'L':
                node = node.left
            elif c == 'R':
                node = node.right
            
            num_steps += 1
            if node is end_node:
                return num_steps
def first():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        instructions, node_map = parse_input(f)
        nodes = build_directed_graph(node_map)
        start_node, end_node = nodes.get('AAA'), nodes.get('ZZZ')
        print(f"Number of steps: {count_steps_to_node(instructions, start_node, end_node)}")

def second():
    print_intro()
    with open(get_input_file_path(), "r") as f:
        instructions, node_map = parse_input(f)
        nodes = build_directed_graph(node_map)
        start_nodes = [node for node in nodes.values() if node.label.endswith('A')]
        current_nodes = start_nodes
        num_steps = 0
        while True:
            for c in instructions:
                updated_nodes = []
                for node in current_nodes:
                    if c == 'L':
                        updated_node = node.left
                    elif c == 'R':
                        updated_node = node.right
                    else:
                        RuntimeError(f"Unknown instruction: {c}")
                    updated_nodes.append(updated_node)
                current_nodes = updated_nodes
                num_steps += 1

                if all(node.label.endswith('Z') for node in current_nodes):
                    print(f"Number of steps: {num_steps}")
                    return            

if __name__ == '__main__':
    first()
    second()
