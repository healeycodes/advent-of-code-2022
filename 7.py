FILE, DIR = "file", "dir"


class Node:
    def __init__(self, type, parent, size=None):
        self.type = type
        self.parent = parent
        self.size = size
        self.children = {}


def parse_ls(current, lines):
    children = {}
    for line in lines:
        if line[0] == "$":
            break
        dir_or_size, name = line.split()
        if dir_or_size == "dir":
            children[name] = Node(DIR, current)
        elif dir_or_size.isnumeric():
            children[name] = Node(FILE, current, int(dir_or_size))
    current.children = children


def find_dir_sizes(node, dir_sizes=[]):
    if node.type == FILE:
        return node.size, FILE, None
    total = 0
    for node in node.children.values():
        size, node_type, _ = find_dir_sizes(node)
        if node_type == DIR:
            dir_sizes.append(size)
        total += size
    return total, DIR, dir_sizes


with open("7.txt") as f:
    root, current = Node(DIR, None), None
    terminal_output = f.read().split("\n")
    for i in range(len(terminal_output)):
        line = terminal_output[i].split()
        if line[0] != "$":
            continue
        if line[1] == "cd":
            target_dir = line[2]
            if target_dir == "/":
                current = root
            elif target_dir == "..":
                current = current.parent
            elif target_dir not in current.children:
                current.children[target_dir] = Node(DIR, current)
            else:
                current = current.children[target_dir]
        elif line[1] == "ls":
            parse_ls(current, terminal_output[i + 1 :])

    used_space, _, dir_sizes = find_dir_sizes(root)
    print(sum(filter(lambda x: x < 100_000, dir_sizes)))

    unused_space, need_at_least = 70_000_000 - used_space, 30_000_000
    print(min(filter(lambda x: unused_space + x > need_at_least, dir_sizes)))
