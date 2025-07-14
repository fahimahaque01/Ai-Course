# গ্রাফটা বানালাম (dictionary দিয়ে)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Depth Limited Search (DFS সীমা দিয়ে)
def dfs_limited(node, target, limit):

    print("Visiting:", node)

    if node == target:
        return True

    if limit == 0:
        return False

    for child in graph.get(node, []):
        if dfs_limited(child, target, limit - 1):
            return True
    return False

# Iterative Deepening DFS
def iddfs(start, target, max_depth):


    for depth in range(max_depth + 1):
         print(f"\n--- Depth Level: {depth} ---") 
        found = dfs_limited(start, target, depth)

        if found:
            print(f"\n✅ Found '{target}' at depth {depth}")
            return True
    print(f"\n❌ '{target}' not found within depth {max_depth}")
    return False

# চালিয়ে দেখি
iddfs('A', 'G', 3)

output............
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


..............Details.........
def dfs_limited(node, target, limit):
    print("Visiting:", node)
    if node == target:
        return True
    if limit == 0:
        return False
    for child in graph.get(node, []):
        if dfs_limited(child, target, limit - 1):
            return True
    return False

এই ফাংশনের কাজ হলো:

একটা নির্দিষ্ট depth (limit) পর্যন্ত DFS চালানো।

যদি node == target হয় → found!

limit 0 হলে আর খোঁজার দরকার নাই → backtrack করো

না হলে graph থেকে child গুলা নিয়ে একটা একটা করে আবার DFS চালাও → limit - 1 দিয়ে।
.......................
def iddfs(start, target, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n--- Depth Level: {depth} ---")
        found = dfs_limited(start, target, depth)
        if found:
            print(f"\n✅ Found '{target}' at depth {depth}")
            return True
    print(f"\n❌ '{target}' not found within depth {max_depth}")
    return False

এখানে কী হচ্ছে:

আমরা depth = 0 থেকে max_depth পর্যন্ত এক এক করে DFS চালাচ্ছি।

প্রতিবার dfs_limited() কল দিচ্ছি নতুন depth limit দিয়ে।

যদি ওই depth-এ খুঁজে পাওয়া যায়, তাহলে ✅ found বলে বন্ধ হয়ে যাবে।

যদি না পাওয়া যায় সব depth শেষে, তাহলে ❌ not found।
........................
iddfs('A', 'G', 3)
 অর্থ: A থেকে শুরু করে G নোডটা খুঁজে দেখো, ৩ লেভেল পর্যন্ত।
