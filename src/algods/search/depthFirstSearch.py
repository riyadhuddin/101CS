graph = {
    '9': set(['5', '6']),
    '5': set(['3', '2']),
    '6': set(['8']),
    ' 3': set([]),
    '2': set(['8']),
    '8': set([])
}
visited = set()


def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS(visited, graph, neighbor)
