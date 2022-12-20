import copy

DATA = 'input_data.txt'
signal = {'20': None, '60': None, '100': None, '140': None, '180': None, '220': None}
x: int = 1
cycle_count: int = 0
with open(DATA) as data:
    for line in data:
        old_x = x
        if line.strip() == 'noop':
            cycle_count += 1
        else:
            cycle_count += 2
            command, value = line.strip().split(' ')
            x += int(value)
        if cycle_count >= 20 and not signal['20']:
            signal['20'] = old_x
        if cycle_count >= 60 and not signal['60']:
            signal['60'] = old_x
        if cycle_count >= 100 and not signal['100']:
            signal['100'] = old_x
        if cycle_count >= 140 and not signal['140']:
            signal['140'] = old_x
        if cycle_count >= 180 and not signal['180']:
            signal['180'] = old_x
        if cycle_count >= 220 and not signal['220']:
            signal['220'] = old_x

total = (20 * signal['20']) + (60 * signal['60']) + (100 * signal['100']) + (140 * signal['140']) + (180 * signal['180']) + (220 * signal['220'])
print(total)