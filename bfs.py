import queue


test_graph = {
    "s" : ["a","b","c"],
    "a" : ["d", "e"],
    "b" : ["g"],
    "c" : ["f"],
    "d" : ["h"],
    "e" : ["g"],
    "f" : ["g"],
    "h" : []
}


def bfs(start, goal, graph):
    visited = []
    queue = []
    path = []

    path.append(start)
    queue.append(start)
    visited.append(start)

    if start == goal:
        path.append(goal)
        return path

    while queue:
        node = queue.pop(0)
        if node == goal:
            return visited
        
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor == goal:
                visited.append(neighbor)
                return visited

            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

path = bfs("s", "g", test_graph)
print(path)