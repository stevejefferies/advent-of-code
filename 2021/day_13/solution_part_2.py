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

for instruction in fold_instructions:
    direction = instruction[0]
    fold_value = instruction[1]
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
    coordinates = final_coordinates

x_length = max(coordinates, key=lambda item: item[0])[0]
y_length = max(coordinates, key=lambda item: item[1])[1]

text_out = []
for i in range(y_length + 1):
    text_out.append(['.']*(x_length+1))

for coordinate in coordinates:
    text_out[coordinate[1]][coordinate[0]] = '#'

for line in text_out:
    print(' '.join(line))
