def areNotTouching(head, tail):
    return max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1

def moveHead(knot, direction):
    match direction:
        case "R":
            return (knot[0], knot[1] + 1)
        case "L":
            return (knot[0], knot[1] - 1)
        case "U":
            return (knot[0] + 1, knot[1])
        case "D":
            return (knot[0] - 1, knot[1])
        case _:
            return knot

def moveTail(head, tail):
    tail_first = tail[0]
    if head[0] > tail[0]:
        tail_first += 1
    elif head[0] < tail[0]:
        tail_first -= 1
    
    tail_second = tail[1]
    if head[1] > tail[1]:
        tail_second += 1
    elif head[1] < tail[1]:
        tail_second -= 1
    
    return (tail_first, tail_second)

def simulateRope(rope, moves):
    grid = set()

    for move in moves:
        direction, magnitude = move.split(" ")
        for _ in range(int(magnitude)):
            rope[0] = moveHead(rope[0], direction)
            for i in range(1, len(rope)):
                if areNotTouching(rope[i - 1], rope[i]):
                    rope[i] = moveTail(rope[i - 1], rope[i])

            grid.add((rope[-1][0], rope[-1][1]))
    
    return len(grid)

with open("day9/input.txt", "r") as day9_input:
    moves = day9_input.readlines()

rope_part1 = [(0, 0) for _ in range(2)]
print("Part 1: " + str(simulateRope(rope_part1, moves)))

rope_part2 = [(0, 0) for _ in range(10)]
print("Part 2: " + str(simulateRope(rope_part2, moves)))