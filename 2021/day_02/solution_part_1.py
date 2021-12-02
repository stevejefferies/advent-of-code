from enum import IntEnum

DATA = 'input_data.txt'

# submarine position
horizontal: int = 0
depth: int = 0


class Depth(IntEnum):
    down = 1
    up = -1


with open(DATA) as data:
    for line in data:
        line = line.lower()
        if line.startswith('forward'):
            horizontal += int(line.split(' ', 1)[1])
        else:
            split_depth = line.split(' ', 1)
            depth += int(Depth[split_depth[0]])*int(split_depth[1])

print(f'Horizontal: {horizontal}')
print(f'Depth: {depth}')
print(f'Total: {horizontal*depth}')
