DATA = 'input_data.txt'

result_mapping = {
    "A": "X", 
    "B": "Y", 
    "C": "Z"
    }

result_score = {
    "X": 1, 
    "Y": 2, 
    "Z": 3
}
opponent_list = ["A", "B", "C"]
result_list = ["X", "Y", "Z"]

total: int = 0

with open(DATA) as data:
    for line in data:
        score = 0
        opponent, play = line.strip().split(" ")
        if play == "X":
            score = 0 + result_score[result_list[opponent_list.index(opponent)-1]]
        elif play == "Y":
            score = 3 + result_score[result_mapping[opponent]]
        else:
            score = 6 + result_score[result_list[opponent_list.index(opponent)-2]]
        total += score

print(total)

