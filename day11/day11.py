import operator
from copy import deepcopy

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

class Monkey:
    def __init__(self):
        self.inspection_count = 0
        self.items = []
        self.operation = None
        self.testDiv = 0
        self.test_true_monkey_index = 0
        self.test_false_monkey_index = 0

    def parseMonkey(self, monkey_data):
        for data in map(lambda a : a.strip(), monkey_data.split("\n")):
            match data.replace(", ", " ").split(" "):
                case ["Starting", "items:", *items]:
                    self.items = list(map(lambda item : int(item), items))
                case ["Operation:", "new", "=", "old", op, val] if val == "old":
                    self.operation = lambda old: ops[op](old, old)
                case ["Operation:", "new", "=", "old", op, val]:
                    self.operation = lambda old: ops[op](old, int(val))
                case ["Test:", "divisible", "by", div]:
                    self.testDiv = int(div)
                case ["If", "true:", "throw", "to", "monkey", true_index]:
                    self.test_true_monkey_index = int(true_index)
                case ["If", "false:", "throw", "to", "monkey", false_index]:
                    self.test_false_monkey_index = int(false_index)
                case _:
                    continue

def throwItemsAround(monkeys, rounds, isPartOne = True):
    chinese_remainder_theroem_constant = 1
    for monkey in monkeys:
        chinese_remainder_theroem_constant *= monkey.testDiv

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                item = monkey.operation(item)
                if isPartOne:
                    item = item // 3
                if item % monkey.testDiv == 0:
                    monkeys[monkey.test_true_monkey_index].items.append(item if isPartOne else item % chinese_remainder_theroem_constant)
                else:
                    monkeys[monkey.test_false_monkey_index].items.append(item if isPartOne else item % chinese_remainder_theroem_constant)
                monkey.items = monkey.items[1:]
                monkey.inspection_count += 1

    monkeys_inspection_count_list_sorted = list(map(lambda monkey : monkey.inspection_count, monkeys))
    monkeys_inspection_count_list_sorted.sort(reverse=True)
    return monkeys_inspection_count_list_sorted[0] * monkeys_inspection_count_list_sorted[1]

with open("day11/input.txt", "r") as day11_input:
    monkeys_data = day11_input.read().split("\n\n")

monkeys = [Monkey() for _ in range(len(monkeys_data))]
for i in range(len(monkeys_data)):
    monkeys[i].parseMonkey(monkeys_data[i])

print("Part 1: " + str(throwItemsAround(deepcopy(monkeys), 20)))

print("Part 2: " + str(throwItemsAround(deepcopy(monkeys), 10000, False)))

