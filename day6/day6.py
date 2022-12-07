def findFirstMarkerPosition(data, distinct_char_count):
    last_chars = list(data[:distinct_char_count])

    for i in range(distinct_char_count, len(data)):
        if len(set(last_chars)) != distinct_char_count:
            last_chars = last_chars[1:]
            last_chars.append(data[i])
        else:
            return i

    return -1

with open("day6/input.txt", "r") as day6_input:
    data = day6_input.read()

first_marker_position_part1 = findFirstMarkerPosition(data, 4)
print("Part 1: " + str(first_marker_position_part1))

first_marker_position_part2 = findFirstMarkerPosition(data, 14)
print("Part 2: " + str(first_marker_position_part2))

    

            

