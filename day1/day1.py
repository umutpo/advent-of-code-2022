def getHighestSum(data, count):
    highest_totals = [0] * count
    current_total = 0
    for current_calorie in data:
        if current_calorie != "":
            current_total += int(current_calorie)
        else:
            for i in range(len(highest_totals)):
                if current_total > highest_totals[i]:
                    highest_totals.insert(i, current_total)
                    highest_totals.pop()
                    break
            current_total = 0
    
    return sum(highest_totals)

with open("day1/input.txt", "r") as day1_input:
    data = day1_input.read().splitlines()

print("Part 1: " + str(getHighestSum(data, 1)))
print("Part 2: " + str(getHighestSum(data, 3)))
