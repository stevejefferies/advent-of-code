import copy

DATA = 'input_data.txt'
signal = {'20': None, '60': None, '100': None, '140': None, '180': None, '220': None}
ticks = [1]
x: int = 1
cycle_count: int = 0
with open(DATA) as data:
    for line in data:
        old_x = x
        ticks.append(old_x)
        if line.strip() == 'noop':
            cycle_count += 1
        else:
            cycle_count += 2
            command, value = line.strip().split(' ')
            x += int(value)
            ticks.append(x)

output_rows =[]
output = ''
for idx, value in enumerate(ticks):
    modifier = len(output_rows)*40
    if abs(value-(idx-modifier)) <= 1:
        output = output + '#'
    else:
        output = output + '*'
    if len(output) == 40:
        output_rows.append(output)
        output = ''

for row in output_rows:
    print(row)