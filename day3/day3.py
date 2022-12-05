def findCommonPriority(rucksacks, count):
    foundTypes = {}
    for i in range(count):
        for current_type in rucksacks[i]:
            if not current_type in foundTypes:
                foundTypes[current_type] = 1 
            elif foundTypes[current_type] == i:
                foundTypes[current_type] = i + 1

    for current_type in foundTypes.keys():
        if foundTypes[current_type] == count:
            if current_type.islower():
                return ord(current_type) - 96
            else:
                return ord(current_type) - 38
    
    return 0

with open("day3/input.txt", "r") as day3_input:
    data = map(lambda rucksack : rucksack.strip(), day3_input.readlines())

total_priority_part1 = 0
total_priority_part2 = 0
currentRucksacks = []
for rucksack in data:
    # Part 1
    rucksack_length = len(rucksack)
    total_priority_part1 += findCommonPriority([rucksack[0 : rucksack_length//2], rucksack[rucksack_length//2 : rucksack_length]], 2)
    # Part 2
    currentRucksacks.append(rucksack)
    if len(currentRucksacks) == 3:
        total_priority_part2 += findCommonPriority(currentRucksacks, 3)
        currentRucksacks.clear()

print("Part 1: " + str(total_priority_part1))
print("Part 2: " + str(total_priority_part2))