import re

def isSubset(pair):
    return (int(pair[0]) >= int(pair[2]) and int(pair[1]) <= int(pair[3])) or (int(pair[0]) <= int(pair[2]) and int(pair[1]) >= int(pair[3]))

def isOverlap(pair):
    return int(pair[1]) >= int(pair[2]) and int(pair[0]) <= int(pair[3])

with open("day4/input.txt", "r") as day4_input:
    data = map(lambda pair : re.split("-|,", pair.strip()), day4_input.readlines())

total_subsets_part1 = 0
total_overlap_part2 = 0
for pair in data:
    if isSubset(pair):
        total_subsets_part1 += 1
    if isOverlap(pair):
        total_overlap_part2 += 1

print("Part 1: " + str(total_subsets_part1))
print("Part 2: " + str(total_overlap_part2))
