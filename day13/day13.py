import ast
from enum import Enum
from functools import cmp_to_key

class PacketOrder(Enum):
    RIGHT_ORDER = 0
    WRONG_ORDER = 1
    CONTINUE = 2

def getPacketOrder(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return PacketOrder.RIGHT_ORDER
        elif left > right:
            return PacketOrder.WRONG_ORDER
        else:
            return PacketOrder.CONTINUE
    elif isinstance(left, int) and isinstance(right, list):
        return getPacketOrder([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return getPacketOrder(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) > 0 and len(right) > 0:
            packetOrder = getPacketOrder(left[0], right[0])
            if packetOrder == PacketOrder.CONTINUE:
                return getPacketOrder(left[1:], right[1:])
            else:
                return packetOrder
        elif len(left) > 0:
            return PacketOrder.WRONG_ORDER
        elif len(right) > 0:
            return PacketOrder.RIGHT_ORDER
        else:
            return PacketOrder.CONTINUE

def arePacketsInRightOrder(left, right):
    packetOrder = getPacketOrder(left, right)
    match packetOrder:
        case PacketOrder.RIGHT_ORDER:
            return -1
        case PacketOrder.WRONG_ORDER:
            return 1
        case _:
            return 0

with open("day13/input.txt") as day13_input:
    pairs = day13_input.read().split("\n\n")

indices_sum_part1 = 0
all_packets_part2 = []
for i in range(len(pairs)):
    left_packet = ast.literal_eval(pairs[i].split("\n")[0])
    all_packets_part2.append(left_packet)

    right_packet = ast.literal_eval(pairs[i].split("\n")[1])
    all_packets_part2.append(right_packet)

    if arePacketsInRightOrder(left_packet, right_packet) == -1:
        indices_sum_part1 += (i + 1)

print("Part 1: " + str(indices_sum_part1))

all_packets_part2.append([[2]])
all_packets_part2.append([[6]])
all_packets_part2 = sorted(all_packets_part2, key=cmp_to_key(arePacketsInRightOrder))

divider1_index = -1
divider2_index = -1
for i in range(len(all_packets_part2)):
    if all_packets_part2[i] == [[2]]:
        divider1_index = i + 1
    elif all_packets_part2[i] == [[6]]:
        divider2_index = i + 1

print("Part 2: " + str(divider1_index * divider2_index))