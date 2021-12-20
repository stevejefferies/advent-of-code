DATA = 'input_data.txt'

template = None
insertion_rules = {}

with open(DATA) as data:
    template = data.readline().strip()
    for line in data.readlines():
        clean_line = line.strip()
        if clean_line:
            key, value = clean_line.split(' -> ', 1)
            insertion_rules[key] = value

char_occurs = {}
for char in template:
    if char in char_occurs.keys():
        char_occurs[char] += 1
    else:
        char_occurs[char] = 1

pairings = {}
for key in insertion_rules.keys():
    pairings[key] = 0

for i in range(len(template)-1):
    sub_string = template[i: i+2]
    pairings[sub_string] += 1

for i in range(10):
    new_pairings = {}
    for key, value in insertion_rules.items():
        if pairings[key]:
            new_pairings[key] = pairings[key]
            pairings[key] = 0
    for key, value in new_pairings.items():
        if insertion_rules[key] in char_occurs.keys():
            char_occurs[insertion_rules[key]] += value
        else:
            char_occurs[insertion_rules[key]] = value
        pairings[key[:1] + insertion_rules[key]] += value
        pairings[insertion_rules[key] + key[1:]] += value


print('Result: ' + str(max(char_occurs.values())-min(char_occurs.values())))
