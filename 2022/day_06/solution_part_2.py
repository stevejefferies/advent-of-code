DATA = 'input_data.txt'

total: int = 0

with open(DATA) as data:
    for line in data:
        buffer = []
        for index, char in enumerate(line):
            if len(buffer) < 14:
                buffer.append(char)
            else:
                buffer.pop(0)
                buffer.append(char)
                if len(buffer) == len(set(buffer)):
                    print(index+1)
                    exit()
