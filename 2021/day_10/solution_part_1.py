DATA = 'input_data.txt'

error_score = 0

stack = []

with open(DATA) as data:
    for line in data:
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
                    error_score += 3
                elif char == ']' and open_char != '[':
                    error_score += 57
                elif char == '}' and open_char != '{':
                    error_score += 1197
                elif char == '>' and open_char != '<':
                    error_score += 25137
                else:
                    continue
                stack.clear()
                break

print('Total error score: ' + str(error_score))
