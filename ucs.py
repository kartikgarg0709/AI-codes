def uniform_cost_search(goal, start, graph):
    queue = []
    answer = 10000   
    queue.append([0, start,[start]])   
    visited = {}      

    while queue:
        queue.sort()
        p = queue.pop(0)

        if p[1] == goal:
            if answer > p[0]:
                answer = p[0]
                path=p[2]
            continue
            
        if p[1] not in visited:
            for neighbor, cost in graph[p[1]].items():
                queue.append([(p[0] + cost), neighbor,p[2]+[neighbor]])
            visited[p[1]] = 1

    return answer,path

# Define the graph as a dictionary
graph = {
    'a': {'b': 2, 'd': 5},
    'b': {'a': 2, 'c': 4, 'd': 5, 'g': 1},
    'c': {'b': 4, 'e': 4, 'f': 6},
    'd': {'a': 5, 'b': 5, 'd': 2, 'g': 6},
    'e': {'c': 4, 'd': 2, 'f': 3, 'g': 7},
    'f': {'c': 6, 'e': 3, 'g': 3},
    'g': {'b': 1, 'd': 6, 'e': 7, 'f': 3}
}

goal = 'g'
answer,path = uniform_cost_search('g', 'a', graph)
print("Minimum cost from 'a' to 'g' is =",path, answer)
