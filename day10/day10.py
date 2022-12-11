def getSignalStrength(cycle, register):
    if cycle == 20 or (cycle - 20) % 40 == 0:
        return cycle * register
    return 0

def drawPixel(cycle, register):
    if abs(cycle - register) <= 1:
        return "#"
    return "."

with open("day10/input.txt", "r") as day10_input:
    commands = day10_input.readlines()

cycle = 0
register = 1
screen = [["."] * 40 for _ in range(6)]

total_signal_strenght_part1 = 0
total_light_pixels_part2 = 0
for command in commands:
    if cycle > 240:
        break

    cycle_needed = 0
    value_added = 0
    match command.strip().split(" "):
        case ["noop"]:
            cycle_needed = 1
        case ["addx", val]:
            cycle_needed = 2
            value_added = int(val)
    
    while cycle_needed > 0:
        cycle += 1
        cycle_needed -= 1
        total_signal_strenght_part1 += getSignalStrength(cycle, register)

        cycle_row = (cycle - 1) // 40
        cycle_index = (cycle - 1) % 40
        screen[cycle_row][cycle_index] = drawPixel(cycle_index, register)
    
    register += value_added

print("Part 1: " + str(total_signal_strenght_part1))

print("Part 2: ")
for row in screen:
    print(''.join(row))