with open("day1_data.txt", "r") as day1_data:
    data = day1_data.read().splitlines()

highest_totals = [0, 0, 0]
current_total = 0
for current_calorie in data:
    if current_calorie == "":
        for i in range(len(highest_totals)):
            if current_total > highest_totals[i]:
                highest_totals.insert(i, current_total)
                highest_totals.pop()
                break
        current_total = 0
    else:
        current_total += int(current_calorie)

print("The sum of highest totals are " + str(sum(highest_totals)))
