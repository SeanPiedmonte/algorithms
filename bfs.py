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

def bfs(graph, goal):
    frontier_list = []
    for key in graph:
        frontier_list.append(key)
        
