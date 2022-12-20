import copy

DATA = 'input_data.txt'

monkey_items = []
monkey_operation = []
monkey_op_val = []
monkey_test = []
monkey_true_output = []
monkey_false_output = []
monkey_inspections = []

with open(DATA) as data:
    for line in data:
        if line.strip().startswith('Starting'):
            start, vals = line.strip().split(':')
            clean_vals = []
            for val in vals.split(','):
                clean_vals.append(int(val.strip()))
            monkey_items.append(clean_vals)
        elif line.strip().startswith('Operation'):
            start, op = line.split('=')
            if '*' in op:
                monkey_operation.append('*')
            elif '+' in op:
                monkey_operation.append('+')
            else:
                raise ValueError()
            op_val = op.strip().split(' ')[-1]
            if op_val == 'old':
                monkey_op_val.append('self')
            else:
                monkey_op_val.append(int(op_val))
        elif line.strip().startswith('Test'):
            monkey_test.append(int(line.strip().split(' ')[-1]))
        elif line.strip().startswith('If true'):
            monkey_true_output.append(int(line.strip().split(' ')[-1]))
        elif line.strip().startswith('If false'):
            monkey_false_output.append(int(line.strip().split(' ')[-1]))

while len(monkey_inspections) < len(monkey_items):
    monkey_inspections.append(0)

for i in range(20):
    for idx, monkey in enumerate(monkey_items):
        for item in monkey:
            if monkey_operation[idx] == '*':
                if monkey_op_val[idx] == 'self':
                    worry = item * item
                else:
                    worry = item * monkey_op_val[idx]
            elif monkey_operation[idx] == '+':
                if monkey_op_val[idx] == 'self':
                    worry = item + item
                else:
                    worry = item + monkey_op_val[idx]
            else:
                raise ValueError()
            worry = int(worry/3)
            if worry % monkey_test[idx] == 0:
                monkey_items[monkey_true_output[idx]].append(worry)
            else:
                monkey_items[monkey_false_output[idx]].append(worry)
            monkey_inspections[idx] += 1
        monkey_items[idx].clear()

monkey_inspections.sort(reverse=True)

print(monkey_inspections[0]*monkey_inspections[1])