DATA = 'input_data.txt'

coordinates = set()
fold_instructions = []

with open(DATA) as data:
    for line in data:
        clean_line = line.strip()
        if clean_line:
            if clean_line.startswith('fold'):
                instructions = clean_line.rsplit(' ', 1)[1].split('=')
                fold_instructions.append((instructions[0], int(instructions[1])))
            else:
                values = clean_line.split(',')
                coordinates.add((int(values[0]), int(values[1])))

direction = fold_instructions[0][0]
fold_value = fold_instructions[0][1]
final_coordinates = set()
for coordinate in coordinates:
    if direction == 'x':
        if coordinate[0] > fold_value:
            final_coordinates.add((fold_value - (coordinate[0] - fold_value), coordinate[1]))
        else:
            final_coordinates.add(coordinate)
    else:
        if coordinate[1] > fold_value:
            final_coordinates.add((coordinate[0], fold_value - (coordinate[1] - fold_value)))
        else:
            final_coordinates.add(coordinate)

print('Number of coordinates: ' + str(len(final_coordinates)))
