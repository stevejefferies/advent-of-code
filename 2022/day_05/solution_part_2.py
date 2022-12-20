DATA = 'input_data.txt'

total: int = 0

raw_stacks = []
instructions = []

with open(DATA) as data:
    found_stack_rows = False
    for line in data:
        if line.strip().startswith('['):
            raw_stacks.append(line)
        else:
            stacks = line.strip().split('   ')
            print(stacks)
            break

start_stack = []
for stack in stacks:
    start_stack.append([])

for row in reversed(raw_stacks):
    idx = 0
    while idx<9:
        string = row[idx*4:(idx+1)*4-1].replace('[', '').replace(']', '').strip()
        if string: start_stack[idx].append(string)
        idx+=1

with open(DATA) as data:
    found_stack_rows = False
    for line in data:            
        if found_stack_rows:
            split_instructions = line.split(' ')
            stack_from = int(split_instructions[3])-1
            stack_to = int(split_instructions[5])-1
            number_to_move = int(split_instructions[1])
            removed_crates = start_stack[stack_from][len(start_stack[stack_from])-number_to_move:]
            start_stack[stack_to] = start_stack[stack_to] + removed_crates
            start_stack[stack_from] = start_stack[stack_from][:len(start_stack[stack_from])-number_to_move]
        else:
            if not line.strip():
                found_stack_rows = True

string = ''
for stack in start_stack:
    string = string + stack[-1]
print(string)
