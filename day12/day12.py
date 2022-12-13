import copy
import sys

class Square:
    def __init__(self, x, y, value, elevation):
        self.x = x
        self.y = y
        self.value = value
        self.elevation = elevation
        self.path_length = sys.maxsize

def checkSuitableNeighbour(x_size, y_size, current_x, current_y, next_x, next_y):
    if next_x < x_size and next_y < y_size and next_x >= 0 and next_y >= 0:
        current_node = grid[current_x][current_y]
        next_node = grid[next_x][next_y]
        return next_node.elevation >= current_node.elevation - 1 and next_node.path_length > current_node.path_length + 1
    
    return False

def getNeighbours(grid, current_x, current_y):
    neighbours = []
    x_size = len(grid)
    y_size = len(grid[0])

    if checkSuitableNeighbour(x_size, y_size, current_x, current_y, current_x + 1, current_y):
        grid[current_x + 1][current_y].path_length = grid[current_x][current_y].path_length + 1
        neighbours.append(grid[current_x + 1][current_y])

    if checkSuitableNeighbour(x_size, y_size, current_x, current_y, current_x, current_y + 1):
        grid[current_x][current_y + 1].path_length = grid[current_x][current_y].path_length + 1
        neighbours.append(grid[current_x][current_y + 1])

    if checkSuitableNeighbour(x_size, y_size, current_x, current_y, current_x - 1, current_y):
        grid[current_x - 1][current_y].path_length = grid[current_x][current_y].path_length + 1
        neighbours.append(grid[current_x - 1][current_y])

    if checkSuitableNeighbour(x_size, y_size, current_x, current_y, current_x, current_y - 1):
        grid[current_x][current_y - 1].path_length = grid[current_x][current_y].path_length + 1
        neighbours.append(grid[current_x][current_y - 1])
    
    return neighbours

def getShortestPathLength(grid, current_x, current_y):
    path_length_to_S = 0
    path_lengths_to_a = []
    queue = []
    queue.append(grid[current_x][current_y])

    grid[current_x][current_y].path_length = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.elevation == ord('a'):
            if current_node.value == 'S':
                path_length_to_S = current_node.path_length
            path_lengths_to_a.append(current_node.path_length)
        
        neighbours = getNeighbours(grid, current_node.x, current_node.y)
        queue.extend(neighbours)

    return (path_lengths_to_a, path_length_to_S)

with open("day12/input.txt", "r") as day12_input:
    data = list(map(lambda row : [d for d in row.strip()], day12_input.readlines()))

grid = [[] for _ in range(len(data))]
start_x, start_y, end_x, end_y = 0, 0, 0, 0
for i in range(len(data)):
    for j in range(len(data[0])):
        grid[i].append(Square(i, j, data[i][j], ord(data[i][j])))
        if data[i][j] == "S":
            start_x = i
            start_y = j
        elif data[i][j] == "E":
            end_x = i
            end_y = j

grid[start_x][start_y].elevation = ord('a')
grid[end_x][end_y].elevation = ord('z')

shortest_paths, path_length_to_S = getShortestPathLength(grid, end_x, end_y)
print("Part 1: " + str(path_length_to_S))
print("Part 2: " + str(min(shortest_paths)))
