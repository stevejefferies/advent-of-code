DATA = 'input_data.txt'

matrix = []
processed = []

def process(line_idx, col_idx, bypass=False):
    if bypass or (line_idx, col_idx) not in processed:
        if not bypass:
            processed.append((line_idx, col_idx))
        if line_idx:
            if col_idx:
                matrix[line_idx - 1][col_idx -1] += 1
                if matrix[line_idx - 1][col_idx -1] > 9:
                    process(line_idx - 1, col_idx -1)
            matrix[line_idx - 1][col_idx] += 1
            if matrix[line_idx - 1][col_idx] > 9:
                process(line_idx - 1, col_idx)
            if col_idx < 9:
                matrix[line_idx - 1][col_idx + 1] += 1
                if matrix[line_idx - 1][col_idx + 1]> 9:
                    process(line_idx - 1, col_idx + 1)
        if line_idx < 9:
            if col_idx:
                matrix[line_idx + 1][col_idx -1] += 1
                if matrix[line_idx + 1][col_idx -1] > 9:
                    process(line_idx + 1, col_idx -1)
            matrix[line_idx + 1][col_idx] += 1
            if matrix[line_idx + 1][col_idx] > 9:
                process(line_idx + 1, col_idx)
            if col_idx < 9:
                matrix[line_idx + 1][col_idx + 1] += 1
                if matrix[line_idx + 1][col_idx + 1] > 9:
                    process(line_idx + 1, col_idx + 1)
        if col_idx:
            matrix[line_idx][col_idx - 1] += 1
            if matrix[line_idx][col_idx - 1] > 9:
                process(line_idx, col_idx - 1)
        if col_idx < 9:
            matrix[line_idx][col_idx + 1] += 1
            if matrix[line_idx][col_idx + 1] > 9:
                process(line_idx, col_idx + 1)

with open(DATA) as data:
    for line in data:
        line_state = []
        for val in list(line.strip()):
            line_state.append(int(val))
        matrix.append(line_state)

flash_total = 0

for i in range(100000):
    #increment all by one
    for line_idx, line in enumerate(matrix):
        for col_idx, col in enumerate(line):
            matrix[line_idx][col_idx] += 1

    for line_idx, line in enumerate(matrix):
        for col_idx, col in enumerate(line):
            if col > 9:
                process(line_idx, col_idx, False)

    # reset all flashed to zero
    step_flash_count = 0
    for line_idx, line in enumerate(matrix):
        for col_idx, col in enumerate(line):
            if col > 9:
                flash_total += 1
                step_flash_count += 1
                matrix[line_idx][col_idx] = 0

    if step_flash_count == 100:
        print('Syncronised flashing after ' + str(i+1) + ' steps')
        exit()

    # clear processing state
    processed.clear()

