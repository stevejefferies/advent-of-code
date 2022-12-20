DATA = 'input_data.txt'

total: int = 0
visible_trees = []
vertical = []
with open(DATA) as data:
    for idx, line in enumerate(data):
        max = -1
        for char_idx, char in enumerate(line.strip()):
            if len(vertical) <= char_idx:
                vertical.append([])
            vertical[char_idx].append(char)
            if int(char) > max:
                visible_trees.append((char_idx, idx))
                max = int(char)
        max = -1
        for char_idx, char in reversed(list(enumerate(line.strip()))):
            if int(char) > max:
                visible_trees.append((char_idx, idx))
                max = int(char)

for idx, line in enumerate(vertical):
    max = -1
    for char_idx, char in enumerate(line):
        if int(char) > max:
            visible_trees.append((idx, char_idx))
            max = int(char)
    max = -1
    for char_idx, char in reversed(list(enumerate(line))):
        if int(char) > max:
            visible_trees.append((idx, char_idx))
            max = int(char)

print(len(visible_trees))
print(len([t for t in (set(tuple(i) for i in visible_trees))]))            
