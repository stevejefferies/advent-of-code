import copy

DATA = 'input_data.txt'

total: int = 0
head = (0,0)
tail = (0,0)
tail_visit = []
with open(DATA) as data:
    for line in data:
        direction, distance = line.strip().split(' ')
        for i in range(int(distance)):
            if direction == 'U':
                head = (head[0], head[1]+1)
            elif direction == 'D':
                head = (head[0], head[1]-1)
            elif direction == 'L':
                head = (head[0]-1, head[1])
            else:
                head = (head[0]+1, head[1])
            
            while not (abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1):
                tail_x = copy.copy(tail[0])
                tail_y = copy.copy(tail[1])
                if direction in ['L', 'R']:
                    tail_y = head[1]
                    if direction == 'L':
                        tail_x -= 1
                    else:
                        tail_x += 1
                else:
                    tail_x = head[0]
                    if direction == 'U':
                        tail_y += 1
                    else:
                        tail_y -= 1
                # if head[0] != tail[0]:
                #     tail_y = head[0]
                # else:
                #     tail_x += 1
                # if head[1] != tail[1]:
                #     tail_x = head[1]
                # else:
                #     tail_y +=1
                tail = (tail_x, tail_y)
            if tail not in tail_visit:
                tail_visit.append(tail)

print(len(tail_visit))