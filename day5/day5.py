import re
from copy import deepcopy

def parseData(data):
    # Parse stacks
    stack_rows = []
    for row in data:
        if row == "\n":
            break

        stack_rows.append(row)
    stack_rows.pop()

    stack_count = len(stack_rows[0]) // 4
    stacks = [[] for i in range(stack_count)]
    for row in stack_rows:
        for i in range(stack_count):
            current_crate = row[(i * 4) + 1]
            if current_crate != " ":
                stacks[i].insert(0, current_crate)

    # Parse moves as [move, from, to]
    move_rows = []
    for row in data:
        move_rows.append(row)

    moves = []
    for row in move_rows:
        moves.append(re.findall(r'\d+', row))

    return stacks, moves

def operateCrane(stacks, moves, advanced_crane=False):
    for move in moves:
        count = int(move[0])
        from_stack = int(move[1]) - 1
        to_stack = int(move[2]) - 1

        moved_crates = []
        for i in range(count):
                if len(stacks[from_stack]) > 0:
                    moved_crates.append(stacks[from_stack].pop())
                else:
                    break
        
        if advanced_crane:
            moved_crates.reverse()
        stacks[to_stack].extend(moved_crates)
                    
    top_crates = ""
    for stack in stacks:
        top_crates += stack.pop() if len(stack) > 0 else " "
        
    return top_crates

with open("day5/input.txt", "r") as day5_input:
    stacks, moves = parseData(iter(day5_input.readlines()))

top_crates_part1 = operateCrane(deepcopy(stacks), moves)
print("Part 1: " + top_crates_part1)

top_crates_part2 = operateCrane(deepcopy(stacks), moves, True)
print("Part 2: " + top_crates_part2)