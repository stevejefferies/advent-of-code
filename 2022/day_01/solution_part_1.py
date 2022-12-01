DATA = 'input_data.txt'

max: int = 0

with open(DATA) as data:
    current: int = 0
    for line in data:
        line = line.strip()
        if line:
            current += int(line)
        else:
            if current > max:
                max = current
            current = 0

print(max)