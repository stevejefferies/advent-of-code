DATA = 'input_data.txt'

total: int = 0

with open(DATA) as data:
    for line in data:
        first, second = line.strip().split(',')
        first_lower, first_upper = [int(s) for s in first.split('-')]
        second_lower, second_upper = [int(s) for s in second.split('-')]
        if set((range(first_lower,first_upper+1))).issubset(range(second_lower,second_upper+1)) or \
            set((range(second_lower,second_upper+1))).issubset(range(first_lower,first_upper+1)):
            total += 1

print(total)
