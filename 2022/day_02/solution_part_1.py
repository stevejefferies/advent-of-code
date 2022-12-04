DATA = 'input_data.txt'

result_mapping = {
    "X": "A", 
    "Y": "B", 
    "Z": "C"
    }

total: int = 0

with open(DATA) as data:
    for line in data:
        score = 0
        opponent, play = line.strip().split(" ")
        play_score = list(result_mapping).index(play)+1
        if result_mapping[play] == opponent:
            score = 3 + play_score
        elif (result_mapping[play] == 'A' and opponent == "C") or (result_mapping[play] == 'B' and opponent == "A") or (result_mapping[play] == 'C' and opponent == "B"):
            score = 6 + play_score
        else:
            score = play_score
        total += score

print(total)

