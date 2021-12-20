DATA = 'input_data.txt'

nodes = {}
visited_nodes = {}


def process_neighbours(graph, distance_graph, coordinate):
    max_coordinate = max(graph)
    if coordinate[0] and (coordinate[0]-1, coordinate[1]) in graph.keys():
        if graph[(coordinate[0]-1,coordinate[1])] > graph[coordinate] + distance_graph[(coordinate[0]-1,coordinate[1])]:
            graph[(coordinate[0]-1,coordinate[1])] = graph[coordinate] + distance_graph[(coordinate[0]-1,coordinate[1])]
    if coordinate[0] < max_coordinate[0] and (coordinate[0] + 1, coordinate[1]) in graph.keys():
        if graph[(coordinate[0] + 1, coordinate[1])] > graph[coordinate] + distance_graph[(coordinate[0] + 1, coordinate[1])]:
            graph[(coordinate[0] + 1, coordinate[1])] = graph[coordinate] + distance_graph[(coordinate[0] + 1, coordinate[1])]
    if coordinate[1] and (coordinate[0],coordinate[1]-1) in graph.keys():
        if graph[(coordinate[0],coordinate[1]-1)] > graph[coordinate] + distance_graph[(coordinate[0],coordinate[1]-1)]:
            graph[(coordinate[0],coordinate[1]-1)] = graph[coordinate] + distance_graph[(coordinate[0],coordinate[1]-1)]
    if coordinate[1] < max_coordinate[1] and (coordinate[0], coordinate[1]+1) in graph.keys():
        if graph[(coordinate[0], coordinate[1]+1)] > graph[coordinate] + distance_graph[(coordinate[0], coordinate[1]+1)]:
            graph[(coordinate[0], coordinate[1]+1)] = graph[coordinate] + distance_graph[(coordinate[0], coordinate[1]+1)]
    val = graph.pop(coordinate)
    return graph

for i in range(5):
    for j in range(5):
        with open(DATA) as data:
            for y_idx, line in enumerate(data):
                for x_idx, val in enumerate(list(line.strip())):
                    risk_val = int(val) + i + j
                    while risk_val > 9:
                        risk_val -= 9
                    nodes[(x_idx + 100*i, y_idx + 100*j)] = risk_val
                    visited_nodes[(x_idx + 100*i, y_idx + 100*j)] = float('inf')

nodes[(0,0)] = 0
visited_nodes[(0, 0)] = 0
max_coordinate = max(visited_nodes)

while len(visited_nodes):
    node = min(visited_nodes, key=visited_nodes.get)

    if node == max_coordinate:
        print('Minimum path: ' + str(visited_nodes[max_coordinate]))
        exit(0)
    visited_nodes = process_neighbours(visited_nodes, nodes, node)

