DATA = 'input_data.txt'
NUMBER_DAYS = 80


def process_day(fish_data):
    output_data = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    to_spawn = fish_data[0]
    for key, value in fish_data.items():
        if key != 0:
            output_data[key - 1] = value
    output_data[6] += to_spawn
    output_data[8] = to_spawn
    return output_data


with open(DATA) as data:
    input_data = data.readline().split(',')
    current_state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for value in input_data:
        current_state[int(value)] += 1

for i in range(NUMBER_DAYS):
    current_state = process_day(current_state)
print(sum(current_state.values()))
