DATA = 'input_data.txt'

def calculate_points(start_x, start_y, end_x, end_y):
    if start_x != end_x and start_y != end_y:
        return []
    if start_x < end_x:
        x_modifier = 1
    else:
        x_modifier = -1
    if start_y < end_y:
        y_modifier = 1
    else:
        y_modifier = -1
    x_distance = abs(end_x - start_x) + 1
    y_distance = abs(end_y - start_y) + 1
    coordinates = []
    for i in range(x_distance):
        for j in range(y_distance):
            x = start_x+i*x_modifier
            y = start_y+j*y_modifier
            coordinate = (x, y)
            coordinates.append(coordinate)
    return coordinates


vent_coordinates = []
duplicate_coordinates = []
duplicate_count = 0

with open(DATA) as data:
    for line in data:
        print(line)
        raw_coords = line.strip().replace('->', ',').split(',')
        new_coordinates = calculate_points(int(raw_coords[0]), int(raw_coords[1]), int(raw_coords[2]), int(raw_coords[3]))
        for coordinate in new_coordinates:
            if coordinate in vent_coordinates:
                if coordinate not in duplicate_coordinates:
                    duplicate_coordinates.append(coordinate)
            else:
                vent_coordinates.append(coordinate)

print(len(duplicate_coordinates))

