import copy

DATA = 'input_data.txt'

error_score = 0
lines = []
stack = []

with open(DATA) as data:
    for line in data:
        stack.clear()
        chars = list(line.strip())
        for char in chars:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char in [')', ']', '}', '>']:
                try:
                    open_char = stack.pop()
                except IndexError:
                    open_char = None
                if char == ')' and open_char != '(':
                    stack.clear()
                    break
                elif char == ']' and open_char != '[':
                    stack.clear()
                    break
                elif char == '}' and open_char != '{':
                    stack.clear()
                    break
                elif char == '>' and open_char != '<':
                    stack.clear()
                    break
                else:
                    continue
        if len(stack):
            lines.append(copy.copy(stack))

stack.clear()

line_totals = []
for line in lines:
    line_total = 0
    for char in reversed(line):
        match char:
            case '(':
                line_total = line_total * 5 + 1
            case '[':
                line_total = line_total * 5 + 2
            case '{':
                line_total = line_total * 5 + 3
            case '<':
                line_total = line_total * 5 + 4
    line_totals.append(line_total)

line_totals.sort()

print('Middle error score: ' + str(line_totals[int((len(line_totals)-1)/2)]))