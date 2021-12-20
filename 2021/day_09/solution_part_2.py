from functools import reduce

DATA = 'input_data.txt'

map_matrix = []
basin_set = set()

class Point:
    def __init__(self, x, y, height, low_point):
        self.x = x
        self.y = y
        self.height = height
        self.low_point = low_point

    def get_basin(self):
        size = 0
        if (self.x, self.y) in basin_set:
            return size
        else:
            basin_set.add((self.x, self.y))
        # above
        if self.y and self.height < map_matrix[self.y - 1][self.x].height < 9:
            size += map_matrix[self.y - 1][self.x].get_basin()
        # below
        if self.y + 1 < len(map_matrix) and self.height < map_matrix[self.y + 1][self.x].height < 9:
            size += map_matrix[self.y + 1][self.x].get_basin()
        # left
        if self.x and self.height < map_matrix[self.y][self.x - 1].height < 9:
            size += map_matrix[self.y][self.x - 1].get_basin()
        # right
        if self.x + 1 < len(map_matrix[0]) and self.height < map_matrix[self.y][self.x + 1].height < 9:
            size += map_matrix[self.y][self.x + 1].get_basin()
        return size + 1


    def is_basin(self):
        if self.low_point:
            return True
        return False


def process(previous_line, current_line, next_line, line_index):
    coordinates = []
    for index, val in enumerate(current_line):
        if index and index + 1 < len(current_line) and val < current_line[index - 1] \
                and val < current_line[index + 1] and val < next_line[index] and val < previous_line[index]:
            coordinates.append(Point(index, line_index, val, True))
        elif not index and val < current_line[index + 1] and val < next_line[index] and val < previous_line[index]:
            coordinates.append(Point(index, line_index, val, True))
        elif not index + 1 < len(current_line) and val < current_line[index - 1] and val < next_line[index] \
                and val < previous_line[index]:
            coordinates.append(Point(index, line_index, val, True))
        else:
            coordinates.append(Point(index, line_index, val, False))
    return coordinates

previous_line = None
current_line = None
next_line = None
final_line = None

points = []
running_index = 0

with open(DATA) as data:
    for string in data:
        line = [int(x) for x in list(string.strip())]
        if not current_line:
            current_line = line
            previous_line = a = [9] * len(line)
            final_line = previous_line
            continue
        elif not next_line:
            next_line = line
        else:
            previous_line = current_line
            current_line = next_line
            next_line = line
        map_matrix.append(process(previous_line, current_line, next_line, running_index))
        running_index += 1

previous_line = current_line
current_line = next_line
next_line = final_line
map_matrix.append(process(previous_line, current_line, next_line, running_index))

basins = []
for line in map_matrix:
    for point in line:
        if point.is_basin():
            basins.append(point.get_basin())
            basin_set.clear()
basins.sort(reverse=True)
print('Score: ' + str(reduce(lambda x, y: x*y, basins[:3])))
