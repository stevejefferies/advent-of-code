DATA = 'input_data.txt'

total: int = 0
binary_values = []


def calc(values, index, keep_common=True):
    if len(values) == 1:
        return values
    zeros = []
    ones = []
    for val in values:
        val_array = list(val)
        if val_array[index] == '0':
            zeros.append(val)
        else:
            ones.append(val)
    if len(ones) >= len(zeros):
        kept_values = ones if keep_common else zeros
    else:
        kept_values = zeros if keep_common else ones
    return calc(kept_values, index+1, keep_common)


with open(DATA) as data:
    for line in data:
        binary_values.append(line.strip())

oxygen_generation = int(calc(binary_values, 0)[0], 2)
CO2_scrubbing = int(calc(binary_values, 0, False)[0], 2)

print('Life Support Rating: ' + str(oxygen_generation*CO2_scrubbing))
