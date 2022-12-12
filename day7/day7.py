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
    for command in commands:
        match command.strip().split(" "):
            case ["$", "cd", ".."]:
                ptr = ptr.parent
            case ["$", "cd", directory]:
                ptr = ptr.get_child(directory)
            case ["dir", directory_name]:
                ptr.add_child(Tree(directory_name, ptr))
            case [file_size, _] if file_size.isnumeric():
                ptr.size += int(file_size)

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
    ptr = dirs_to_check.pop() if len(dirs_to_check) > 0 else None

print("Part 1: " + str(total_part1))
print("Part 2: " + str(smallest_needed_part2))