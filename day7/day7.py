class Tree(object):
    def __init__(self, name='/', parent=None):
        self.name = name
        self.size = 0
        self.parent = parent
        self.children = []
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    def get_size(self):
        return self.size + sum(list(map(lambda node : node.get_size(), self.children)))

def executeCommands(root, commands):
    ptr = root
    ls_mode = False
    for current_command in commands:
        split_line = current_command.strip().split(" ")
        if split_line[0] == "$":
            ls_mode = False
            if split_line[1] == "cd":
                if split_line[2] == "..":
                    ptr = ptr.parent
                else:
                    ptr = ptr.get_child(split_line[2])
            elif split_line[1] == "ls":
                ls_mode = True
        elif ls_mode:
            if split_line[0] == "dir":
                ptr.add_child(Tree(split_line[1], ptr))
            elif split_line[0].isnumeric():
                ptr.size += int(split_line[0])

with open("day7/input.txt", "r") as day7_input:
    data = day7_input.readlines()

root = Tree("/")
executeCommands(root, data[1:])

total_part1 = 0
smallest_needed_part2 = 70000000
NEEDED_SPACE = 30000000 - (70000000 - root.get_size())

ptr = root
dirs_to_check = []
while ptr != None:
    current_size = ptr.get_size()
    if current_size <= 100000:
        total_part1 += current_size
    if current_size >= NEEDED_SPACE and current_size <= smallest_needed_part2:
        smallest_needed_part2 = current_size

    dirs_to_check.extend(ptr.children)
    if len(dirs_to_check) > 0:
        ptr = dirs_to_check.pop()
    else:
        ptr = None

print("Part 1: " + str(total_part1))
print("Part 2: " + str(smallest_needed_part2))