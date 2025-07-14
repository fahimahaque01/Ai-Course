# Algorithm Implementations Guide

---

## BFS (Breadth-First Search)

**How it works:**
BFS explores a graph level by level, starting from a source node and visiting all its neighbors before moving to the next level. It uses a queue to keep track of nodes to visit next.

**Applications:**
- Shortest path in unweighted graphs
- Web crawlers
- Social network analysis
- Finding connected components

**Complexity:**
- Time: O(V + E) (V = vertices, E = edges)
- Space: O(V)

**How to run:**
```
python BFS.py
```
**Demo Output:**
```
Visiting: A
Visiting: B
Visiting: C
Visiting: D
Visiting: E
Visiting: F
Visiting: G
```

---

## DFS (Depth-First Search)

**How it works:**
DFS explores as far as possible along each branch before backtracking. It uses recursion or a stack to keep track of the path.

**Applications:**
- Topological sorting
- Cycle detection
- Path finding in mazes
- Connected components

**Complexity:**
- Time: O(V + E)
- Space: O(V)

**How to run:**
```
python DFS.py
```
**Demo Output:**
```
Visiting: A
Visiting: B
Visiting: D
Visiting: E
Visiting: G
Visiting: C
Visiting: F
```

---

## Best-First Search

**How it works:**
Best-First Search uses a priority queue to explore the most promising node (based on a heuristic) first. It is a greedy algorithm.

**Applications:**
- Pathfinding (e.g., GPS navigation)
- AI in games
- Puzzle solving

**Complexity:**
- Time: O(E log V) (depends on heuristic and implementation)
- Space: O(V)

**How to run:**
```
python BestFirst.py
```
**Demo Output:**
```
Visiting: A
Visiting: B
Visiting: E
Visiting: G
🎯 Goal reached: G
```

---

## Beam Search

**How it works:**
Beam Search is a heuristic search like BFS but only keeps the best k nodes at each level (beam width). It reduces memory usage by pruning less promising nodes.

**Applications:**
- Natural Language Processing (NLP)
- Speech recognition
- AI planning

**Complexity:**
- Time: O(k^d) (k = beam width, d = depth)
- Space: O(kd)

**How to run:**
```
python BeamSearch.py
```
**Demo Output:**
```
Current Beam: ['A']
Current Beam: ['C', 'D']
Current Beam: ['G', 'H']
✅ Found goal: G
```

---

## Alpha-Beta Pruning

**How it works:**
Alpha-Beta Pruning is an optimization for the Minimax algorithm. It eliminates branches in the game tree that cannot possibly affect the final decision, improving efficiency.

**Applications:**
- Game AI (chess, tic-tac-toe, etc.)
- Decision making in adversarial environments

**Complexity:**
- Time: O(b^d) (b = branching factor, d = depth), but much less in practice due to pruning
- Space: O(d)

**How to run:**
- Edit `AlphaBheta.py` to define your game tree and helper functions.
- Call the minimax function as shown in the file.

**Demo Output:**
- Depends on your implementation and input.

---

## Minimax

**How it works:**
Minimax is a recursive algorithm for decision making in two-player games. It assumes both players play optimally and chooses moves to maximize the minimum gain.

**Applications:**
- Game AI (tic-tac-toe, chess, etc.)
- Adversarial search

**Complexity:**
- Time: O(b^d)
- Space: O(d)

**How to run:**
```
python minmax.py
```
**Demo Output:**
```
সেরা ফলাফল: 9
```

---

## Iterative Deepening Search

**How it works:**
Combines the space efficiency of DFS with the optimality of BFS. It repeatedly runs DFS with increasing depth limits until the goal is found.

**Applications:**
- Game tree search
- Pathfinding with unknown depth

**Complexity:**
- Time: O(b^d)
- Space: O(d)

**How to run:**
```
python IterativeDeepingSearch.py
```
**Demo Output:**
```
--- Depth Level: 0 ---
Visiting: A

--- Depth Level: 1 ---
Visiting: A
Visiting: B
Visiting: C

--- Depth Level: 2 ---
Visiting: A
Visiting: B
Visiting: D
Visiting: E
Visiting: C
Visiting: F

--- Depth Level: 3 ---
Visiting: A
Visiting: B
Visiting: D
Visiting: E
Visiting: G

✅ Found 'G' at depth 3
```

---

## Depth-Limited Search

**How it works:**
A variant of DFS with a predetermined depth limit. It explores nodes up to a certain depth and backtracks if the limit is reached.

**Applications:**
- Game tree search with limited lookahead
- Pathfinding with resource constraints

**Complexity:**
- Time: O(b^l) (l = depth limit)
- Space: O(l)

**How to run:**
```
python DpethLimitSearch.py
```
**Demo Output:**
```
Visiting: A | Depth Limit: 2
Visiting: B | Depth Limit: 1
Visiting: D | Depth Limit: 0
Visiting: E | Depth Limit: 0
Visiting: C | Depth Limit: 1
Visiting: F | Depth Limit: 0

❌ 'G' NOT found within depth 2
```
