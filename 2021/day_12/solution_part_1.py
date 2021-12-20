import copy

DATA = 'input_data.txt'

graph = {}

with open(DATA) as data:
    for line in data:
        start, end = line.strip().split('-', 1)
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
        if end in graph:
            graph[end].append(start)
        else:
            graph[end] = [start]

visited_nodes = []
paths = []


def depth_first_search(visited_nodes, graph, node):
    if node not in visited_nodes or node.isupper():
        visited_nodes.append(node)
        if node == 'end':
            paths.append(copy.deepcopy(visited_nodes))
        else:
            for neighbour in graph[node]:
                depth_first_search(visited_nodes, graph, neighbour)
        visited_nodes.remove(node)


depth_first_search(visited_nodes, graph, 'start')
print('Total paths: ' + str(len(paths)))
