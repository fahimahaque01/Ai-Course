def dfs(graph, start, visited=None):

    if visited is None:// first node kina check kora or.
        visited = set() //visited set banani oise

    print("Visiting:", start) 

    visited.add(start)

    for neighbor in graph[start]: //shobgula connected node re bair kori aner
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) //visited na oile backtracking

# 🔍 গ্রাফ
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# ▶️ DFS চালাও
dfs(graph, 'A')
