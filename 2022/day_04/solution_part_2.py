DATA = 'input_data.txt'

total: int = 0

with open(DATA) as data:
    for line in data:
        first, second = line.strip().split(',')
        first_lower, first_upper = [int(s) for s in first.split('-')]
        second_lower, second_upper = [int(s) for s in second.split('-')]
        if max(first_lower, second_lower) <= min(first_upper, second_upper):
            total +=1

print(total)
