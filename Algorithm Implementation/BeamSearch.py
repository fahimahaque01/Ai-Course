Beam Search হলো একধরনের heuristic search algorithm।
এটা একটু বুদ্ধিমান BFS এর মতো, কিন্তু সবগুলো node expand না করে শুধুমাত্র best k টা node (beam width) রাখে।

 কীভাবে কাজ করে?
শুরু node থেকে শুরু করবি।

এক লেভেল নিচে যতগুলো child আসে, তাদের মধ্যে heuristic মান দেখে বেছে নিবে শুধু k টা best node।

ওই k টা node দিয়েই পরের লেভেল চালাবে।

target পেলে থেমে যাবে।

# Simple graph with heuristic values
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values for each node (lower = better)
heuristics = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0,   # 🎯 Target node
    'H': 3
}

def beam_search(start, goal, beam_width):
    queue = [start]
    while queue:
        print("\nCurrent Beam:", queue)
        if goal in queue:
            print(f"✅ Found goal: {goal}")
            return True
        
        # Next level candidates
        next_level = []
        for node in queue:
            next_level.extend(graph.get(node, []))

        # Sort by heuristic and take best k nodes
        next_level = sorted(next_level, key=lambda x: heuristics[x])
        queue = next_level[:beam_width]
    
    print(f"❌ Goal '{goal}' not found.")
    return False

# Run the beam search
beam_search('A', 'G', beam_width=2)


অবশ্যই সুমন! নিচে Beam Search এর কোডটা ধাপে ধাপে, সহজ ভাষায় বুঝিয়ে দিলাম। এটা বুঝলে future-এ NLP, speech recognition, even AI image captioning-এ ব্যবহার করতে পারবি।

def beam_search(start, goal, beam_width):
    queue = [start]

 Beam Search একটা queue দিয়ে কাজ করে।
এখানে প্রথমে শুধু A থাকবে queue-তে।

    while queue:
        print("\nCurrent Beam:", queue)
        if goal in queue:
            print(f"✅ Found goal: {goal}")
            return True
🔁 যতক্ষণ queue ফাঁকা না হয়, ততক্ষণ চালিয়ে যাব।
✅ যদি goal queue-তে থাকে → কাজ শেষ → True return।

        next_level = []
        for node in queue:
            next_level.extend(graph.get(node, []))

📚 প্রত্যেক beam-এর জন্য তার child গুলা বের করি।
যেমন A → B, C, D

        next_level = sorted(next_level, key=lambda x: heuristics[x])
        queue = next_level[:beam_width]

🧠 এই অংশেই Beam Search-এর বুদ্ধি:

সব child গুলা heuristic দিয়ে sort করলাম (কম মান আগে)

তার মধ্যে থেকে শুধু beam_width টা best node রাখলাম

যেমনঃ beam_width = 2 হলে → G আর F যদি ভালো হয়, ওগুলোই রাখবে।
    print(f"❌ Goal '{goal}' not found.")
    return False
❌ যদি শেষ পর্যন্ত target পাওয়া না যায় → False return

beam_search('A', 'G', beam_width=2)
🧠 A → C, D (heuristics: 4, 5) → C-তে G → ✅ G found!

