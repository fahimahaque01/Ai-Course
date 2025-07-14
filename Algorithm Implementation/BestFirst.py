import heapq  # priority queue ব্যবহারের জন্য

def best_first_search(graph, start, goal, heuristic):
    visited = set()  # যেসব node আমরা আগেই দেখে ফেলেছি
    queue = [(heuristic[start], start)]  # priority queue (min-heap)

    while queue:
        _, current = heapq.heappop(queue)  # heuristic মান সবচেয়ে কম যেটা, ওটা বের করি
        print("Visiting:", current)

        if current == goal:
            print("🎯 Goal reached:", current)
            return

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic[neighbor], neighbor))

    print("❌ Goal not found")

# 🔍 গ্রাফ (adjacency list আকারে)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# 🎯 heuristic মান (যত ছোট, তত ভালো)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 6,
    'G': 0  # goal node
}

# ▶️ function call
best_first_search(graph, 'A', 'G', heuristic)

# গ্রাফ
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# heuristic values (goal: D)
heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 0
}

best_first_search(graph, 'A', 'D', heuristic)

def best_first_search(...)
এখানে আমরা আমাদের মূল function বানাচ্ছি — ৪টা ইনপুট নিচ্ছে:

graph → গ্রাফটা (node গুলোর সংযোগ)

start → কোথা থেকে শুরু করব

goal → গন্তব্য কোথায়

heuristic → কোন node goal থেকে কতটা দূরে, সেই ধারণা


✅ visited = set()
যেসব node আমরা আগেই ঘাঁটেছি, সেগুলা এই visited সেটে রাখব — যাতে বারবার একই জায়গায় না যাই।

queue = [(heuristic[start], start)]
আমাদের priority queue শুরু হচ্ছে — যার প্রথম মান start node আর তার heuristic মান।

👉 এটা মিন-হিপের মতো কাজ করে, মানে যেটার মান (distance) সবচেয়ে কম, ওটাকেই আগে বের করবে।


 while queue:
যতক্ষণ queue-তে কিছু আছে, আমরা একে একে node বের করে ঘাঁটব।

এখানে queue থেকে heuristic মান অনুযায়ী সর্বোত্তম (সর্বনিম্ন মানওয়ালা) node টা বের করে আনছি।

if current == goal:
যদি এখন যে node টা দেখছি, ওটাই গন্তব্য হয় — তাহলে খোঁজা শেষ!


 if current not in visited:
যদি node টা এখনো আমরা ঘাঁটিনি, তাহলে:

✅ visited.add(current) → ঘাঁটা হয়ে গেছে, বলে রাখি।

✅ for neighbor in graph[current] → এর প্রতিবেশি node গুলা ঘাঁটি

✅ heapq.heappush(...) → neighbor গুলা queue তে ঢুকিয়ে দেই, ওদের heuristic অনুযায়ী।


