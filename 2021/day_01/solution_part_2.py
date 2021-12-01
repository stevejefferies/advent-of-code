DATA = 'input_data.txt'
WINDOW_SIZE = 3

depth_increased: int = 0

num_lines = sum(1 for line in open(DATA))

with open('input_data.txt') as data:
    lines = [int(x.strip()) for x in data.readlines()]
    previous: int = None
    for i in range(num_lines - (WINDOW_SIZE-1)):
        window = sum(lines[i:i+WINDOW_SIZE])
        if previous and window > previous:
            depth_increased += 1
        previous = window

print(depth_increased)