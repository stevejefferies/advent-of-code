DATA = 'input_data.txt'

total: int = 0
bit_count = []

with open(DATA) as data:
    for line in data:
        total += 1
        for idx, bit in enumerate(line.strip()):
            bit_int = int(bit)
            if len(bit_count) > idx:
                bit_count[idx] += bit_int
            else:
                bit_count.append(bit_int)

binary_vals = []
for val in bit_count:
    if val > total/2:
        binary_vals.append('1')
    else:
        binary_vals.append('0')

gamma = ''.join(binary_vals)
epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

print('Power consumption: ' + str(int(gamma, 2)*int(epsilon, 2)))
