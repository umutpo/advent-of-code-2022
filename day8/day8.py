import numpy

def maxInList(list):
    return max(list) if len(list) > 0 else -1

with open("day8/input.txt", "r") as day8_input:
    data = numpy.array(list(map(lambda row : [int(d) for d in row.strip()], day8_input.readlines())))
    row_size, column_size = data.shape

# Part 1
highest_from_left = [[] for i in range(row_size)]
highest_from_right = [[] for i in range(row_size)]
highest_from_top = [[] for i in range(row_size)]
highest_from_bottom = [[] for i in range(row_size)]

for row_index in range(row_size):
    for column_index in range(column_size):
        highest_from_left[row_index].append(maxInList(data[row_index, 0:column_index]))
        highest_from_right[row_index].append(maxInList(data[row_index, (column_index + 1):column_size]))
        highest_from_top[row_index].append(maxInList(data[0:row_index, column_index]))
        highest_from_bottom[row_index].append(maxInList(data[(row_index + 1):row_size, column_index]))

total_visible_trees_part1 = 0
for row_index in range(row_size):
    for column_index in range(column_size):
        min_tree_size = min([highest_from_left[row_index][column_index],
                             highest_from_right[row_index][column_index], 
                             highest_from_top[row_index][column_index], 
                             highest_from_bottom[row_index][column_index]])
        if data[row_index][column_index] > min_tree_size:
            total_visible_trees_part1 = total_visible_trees_part1 + 1

print("Part 1: " + str(total_visible_trees_part1))

# Part 2
highest_scenic_score_part2 = 0
for row_index in range(1, row_size):
    for column_index in range(1, column_size):
        current_tree = data[row_index][column_index]
        
        left_scenery = 0
        for i in range(column_index - 1, -1, -1):
            if current_tree <= data[row_index, i]:
                left_scenery += 1
                break
            left_scenery += 1
        
        right_scenery = 0
        for i in range(column_index + 1, column_size):
            if current_tree <= data[row_index, i]:
                right_scenery += 1
                break
            right_scenery += 1
        
        top_scenery = 0
        for i in range(row_index - 1, -1, -1):
            if current_tree <= data[i, column_index]:
                top_scenery += 1
                break
            top_scenery += 1

        bottom_scenery = 0
        for i in range(row_index + 1, row_size):
            if current_tree <= data[i,  column_index]:
                bottom_scenery += 1
                break
            bottom_scenery += 1

        scenery = left_scenery * right_scenery * top_scenery * bottom_scenery
        if (scenery > highest_scenic_score_part2):
            highest_scenic_score_part2 = scenery

print("Part 2: " + str(highest_scenic_score_part2))