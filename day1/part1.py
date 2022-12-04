with open("day1_data.txt", "r") as day1_data:
    data = day1_data.read().splitlines()

highest_total = 0
current_total = 0
for current_calorie in data:
    if current_calorie == "":
        if current_total > highest_total:
            highest_total = current_total
        current_total = 0
    else:
        current_total += int(current_calorie)
print("Highest total is " + str(highest_total))