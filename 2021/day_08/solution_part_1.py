DATA = 'input_data.txt'

total = 0

with open(DATA) as data:
    for line in data:
        for val in line.split('|', 1)[1].split():
            if len(val) in [2, 3, 4, 7]:
                total += 1

print('Total instances of 1, 4, 7, 8: ' + str(total))
