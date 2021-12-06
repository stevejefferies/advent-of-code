import copy

NUMBER_INPUT = 'input_numbers.txt'
CARD_INPUT = 'bingo_cards.txt'

cards = []


class BingoCard:

    def __init__(self, card_input):
        self.total = 0
        self.columns = []
        self.rows = copy.copy(card_input)
        for row_idx, row in enumerate(card_input):
            self.total += sum(row)
            for col_idx, val in enumerate(row):
                if len(self.columns) > col_idx:
                    self.columns[col_idx].append(val)
                else:
                    self.columns.append([val])

    def process(self, number):
        found = False
        for row in self.rows:
            if number in row:
                row.remove(number)
                found = True
                if len(row) == 0:
                    self.total -= number
                    return self.total * number
        for col in self.columns:
            if number in col:
                col.remove(number)
                found = True
                if len(col) == 0:
                    self.total -= number
                    return self.total * number
        if found:
            self.total -= number

with open(CARD_INPUT) as card_data:
    card_set = []
    for line in card_data:
        if len(line.strip()) == 0:
            continue
        numbers = [int(x) for x in line.strip().split()]
        card_set.append(numbers)
        if len(card_set) == 5:
            cards.append(BingoCard(card_set))
            card_set.clear()

with open(NUMBER_INPUT) as numbers:
    for line in numbers:
        for number in line.split(','):
            for card in cards:
                result = card.process(int(number))
                if result:
                    print(result)
                    exit(0)
