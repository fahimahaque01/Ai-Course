from collections import deque

def bfs(graph, start):
    visited = set()  # visited set to track visited nodes
    queue = deque([start])  # queue to manage the exploration order

    while queue:
        node = queue.popleft()  # pop the leftmost node from queue

        if node not in visited:
            print("Visiting:", node)
            visited.add(node)  # mark node as visited

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # add neighbors to queue

# ----------------- Test Graph -----------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# ----------------- Run BFS -----------------
bfs(graph, 'A')
