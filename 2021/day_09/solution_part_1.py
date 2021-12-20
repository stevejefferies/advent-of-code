DATA = 'input_data.txt'


def process(previous_line, current_line, next_line):
    running_total = 0
    for index, val in enumerate(current_line):
        if index and index + 1 < len(current_line) and val < current_line[index - 1] \
                and val < current_line[index + 1] and val < next_line[index] and val < previous_line[index]:
            running_total += val + 1
        elif not index and val < current_line[index + 1] and val < next_line[index] and val < previous_line[index]:
            running_total += val + 1
        elif not index + 1 < len(current_line) and val < current_line[index - 1] and val < next_line[index] \
                and val < previous_line[index]:
            running_total += val + 1
    return running_total

previous_line = None
current_line = None
next_line = None
final_line = None

total = 0

with open(DATA) as data:
    for string in data:
        line = [int(x) for x in list(string.strip())]
        if not current_line:
            current_line = line
            previous_line = a = [9] * len(line)
            final_line = previous_line
            continue
        elif not next_line:
            next_line = line
        else:
            previous_line = current_line
            current_line = next_line
            next_line = line
        total += process(previous_line, current_line, next_line)

previous_line = current_line
current_line = next_line
next_line = final_line
total += process(previous_line, current_line, next_line)

print('Total: ' + str(total))
