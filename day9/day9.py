def moveKnot(knot, direction):
    match direction:
            case 'R':
                knot[0] = (knot[0] + 1) % 5
            case 'L':
                knot[0] = (knot[0] - 1) % 5
            case 'U':
                knot[1] = (knot[1] + 1) % 4
            case 'D':
                knot[1] = (knot[1] - 1) % 4 
    return knot

with open("day9/input.txt", "r") as day9_input:
    data = day9_input.readlines()

grid = [[False]*6 for i in range(5)]
head = [0, 0]
tail = [0, 0]

for move in data:
    direction = move[0]
    magnitude = int(move[2])
    while magnitude > 0:
        areTheyDiagonal = abs(head[0] - tail[0]) >= 1 and abs(head[1] - tail[1]) >= 1
        head = moveKnot(head, direction)
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            if areTheyDiagonal:
                if direction == 'R' or direction == 'L':
                    tail = moveKnot(tail, 'U') if head[1] - tail[1] > 0 else moveKnot(tail, 'D')
                else:
                    tail = moveKnot(tail, 'R') if head[0] - tail[0] > 0 else moveKnot(tail, 'L')
            tail = moveKnot(tail, direction)
        
        grid[tail[0]][tail[1]] = True
        magnitude -= 1

total_visited_part1 = 0
for i in range(5):
    for j in range(6):
        if grid[i][j]:
            total_visited_part1 += 1

print("Part 1: " + str(total_visited_part1))