import copy

DATA = 'input_data.txt'

def update_tail(head, tail):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        new_x = tail[0]
        new_y = tail[1]
        if head[0] > tail[0]:
            new_x += 1
        elif head[0] < tail[0]:
            new_x -= 1
        if head[1] > tail[1]:
            new_y +=1
        elif head[1] < tail[1]:
            new_y -= 1
        return (new_x, new_y)
    else:
        return tail


total: int = 0
knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
tail_visit = []
with open(DATA) as data:
    for line in data:
        direction, distance = line.strip().split(' ')
        head = copy.copy(knots[0])
        for i in range(int(distance)):
            if direction == 'U':
                head = (head[0], head[1]+1)
            elif direction == 'D':
                head = (head[0], head[1]-1)
            elif direction == 'L':
                head = (head[0]-1, head[1])
            else:
                head = (head[0]+1, head[1])
            knots[0] = head
            new_dir = direction

            for idx, knot in enumerate(knots[1:]):
                head2 = knots[idx]
                tail = knots[idx+1]

                knots[idx+1] = update_tail(head2, tail)

                if idx == 8 and knots[-1] not in tail_visit:
                    tail_visit.append(knots[-1])

print(len(tail_visit))