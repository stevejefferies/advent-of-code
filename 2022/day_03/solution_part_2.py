from itertools import zip_longest

DATA = 'input_data.txt'

lookup = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

total: int = 0

def group(iterable):
    args = [iter(iterable)] * 3
    return zip_longest(*args)

with open(DATA) as data:
    for lines in group(data):
        for i in lines[0]:
            if i in lines[1] and i in lines[2]:
                score = lookup[i.lower()]
                if i.lower() != i:
                    score += 26
                total += score
                break

print(total)
