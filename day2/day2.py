def getGameScore(game):
    first_column_move = ord(game[0]) - 64
    second_column_move = ord(game[1]) - 87
    difference = first_column_move - second_column_move

    # Rock: 1 / Paper: 2 / Scissors: 3
    winning_score = 0
    if difference == -2:
        winning_score = 0 
    elif difference == -1:
        winning_score = 6
    elif difference == 0:
        winning_score = 3
    elif difference == 1:
        winning_score = 0 
    elif difference == 2:
        winning_score = 6

    return winning_score + second_column_move

def chooseCorrectMove(game):
    first_column_move = ord(game[0]) - 64

    # X: Lose / Y: Draw / Z: Win
    chosen_move = first_column_move + 87
    if game[1] == 'X':
        if first_column_move - 1 > 0:
            return chr(chosen_move - 1) 
        else: 
            return chr(chosen_move + 2)
    elif game[1] == 'Y':
        return chr(chosen_move)
    elif game[1] == 'Z':
        if first_column_move + 1 < 4:
            return chr(chosen_move + 1) 
        else:
            return chr(chosen_move - 2)

with open("day2/input.txt", "r") as day2_input:
    data = map(lambda game : game.split(), day2_input.readlines())

total_score_part1 = 0
total_score_part2 = 0
for game in data:
    # Part 1 Calculation
    total_score_part1 += getGameScore(game)
    # Part 2 Calculation
    game[1] = chooseCorrectMove(game)
    total_score_part2 += getGameScore(game)

print("Part 1: " + str(total_score_part1))
print("Part 2: " + str(total_score_part2))