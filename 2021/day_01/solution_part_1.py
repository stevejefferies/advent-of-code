DATA = 'input_data.txt'

depth_increased: int = 0

with open(DATA) as data:
    previous: int = None
    for line in data:
        num_data = int(line.split()[0])
        if previous and num_data > previous:
            depth_increased += 1
        previous = num_data

print(depth_increased)
