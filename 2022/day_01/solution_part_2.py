DATA = 'input_data.txt'

max_list: list = [0]*3

with open(DATA) as data:
    current: int = 0
    for line in data:
        line = line.strip()
        if line:
            current += int(line)
        else:
            if current > max_list[0]:
                max_list[0] = current
            current = 0
            max_list.sort()

for item in max_list:
    print(item)
print(sum(max_list))