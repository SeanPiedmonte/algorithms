from typing import Dict, List



test_graph = {
    "s" : ["a", "b", "c"],
    "a" : ["d", "e"],
    "b" : ["g"],
    "c" : ["f"],
    "d" : ["h"],
    "e" : ["g"],
    "f" : ["g"]
}


def bfs(graph, node1, node2):
    paths = [[node1]]
    index = 0
    visited = [node1]

    if node1 == node2:
        return paths[0]
    
    while index < len(paths):
        path = paths[index]
        last = path[-1]
        next = graph[last]

        if node2 in next:
            path.append(node2)
            return path
        
        for node in next:
            if next not in visited:
                new_path = path[:]
                new_path.append(node)
                visited.append(node)
        

                
        index += 1
    return []

path = bfs(test_graph, "s", "g")
print(path)