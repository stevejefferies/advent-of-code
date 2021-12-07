DATA = 'input_data.txt'

with open(DATA) as data:
    input_data = data.readline().split(',')

max_position = int(max(input_data))
min_position = int(min(input_data))

min_movement = None


# Calculate total number in triangle sequence based on number in sequence
def triangle(number):
    total = 0
    for i in range(number):
        total += i+1
    return total


for end_position in range(min_position, max_position):
    total_movement = 0
    for crab in input_data:
        total_movement += triangle(abs(int(crab)-end_position))
    if not min_movement or total_movement < min_movement:
        min_movement = total_movement

print('Minimum fuel usage: ' + str(min_movement))
