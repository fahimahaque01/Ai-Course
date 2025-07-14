Depth-Limited Search (DLS) হলো একটি DFS (Depth-First Search) এর রূপ, যেখানে আমরা বলে দিই "এই গহীনতার বেশি তুমি যেও না!"

✅ উপযোগিতা (When to Use DLS):
আমরা যদি জানি বা অনুমান করতে পারি যে সমাধান একটা নির্দিষ্ট গভীরতার মধ্যে আছে, তখন DLS ব্যবহার করি।

এটি DFS এর মতোই কাজ করে, কিন্তু নির্ধারিত depth limit-এর বাইরে আর যায় না।


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def depth_limited_search(node, target, limit):
    print("Visiting:", node, "| Depth Limit:", limit)
    if node == target:
        return True
    if limit == 0:
        return False
    for child in graph.get(node, []):
        if depth_limited_search(child, target, limit - 1):
            return True
    return False

# Call the function
start = 'A'
goal = 'G'
depth_limit = 2

found = depth_limited_search(start, goal, depth_limit)

if found:
    print(f"\n✅ '{goal}' found within depth {depth_limit}")
else:
    print(f"\n❌ '{goal}' NOT found within depth {depth_limit}")

......output..............
Visiting: A | Depth Limit: 2
Visiting: B | Depth Limit: 1
Visiting: D | Depth Limit: 0
Visiting: E | Depth Limit: 0
Visiting: C | Depth Limit: 1
Visiting: F | Depth Limit: 0

❌ 'G' NOT found within depth 2
..........Details.............
def depth_limited_search(node, target, limit):
    print("Visiting:", node, "| Depth Limit:", limit)
প্রতিবার যখন কোন node-এ যাওয়া হয়, তখন সেটা print করে — যেন বুঝতে পারিস কোন node-এ ঢুকেছে আর depth কত।

    if node == target:
        return True
✅ যদি বর্তমানে যেই node-এ আছি, ওটাই যদি target হয় (যেমন G), তাহলে True দিয়ে function শেষ।

    if limit == 0:
        return False
⚠️ যদি depth limit 0 হয়, মানে আর গভীর যাওয়ার অনুমতি নাই → তাই False ফেরত দিয়ে ফিরে আসি।

    for child in graph.get(node, []):
        if depth_limited_search(child, target, limit - 1):
            return True
🔁 বর্তমান node-এর সব child নোডে এক এক করে ঢুকি।
প্রতিবার limit - 1 করে দিই, কারণ একধাপ নিচে যাচ্ছি।

যদি কোনও একটা child node-এর ভেতরেই target পেয়ে যাই, তাহলে True ফেরত দিয়ে উপরের দিকে উঠে আসি।

    return False
❌ যদি সব child check করার পরও কিছু না পাই, তাহলে False রিটার্ন করি।

start = 'A'
goal = 'G'
depth_limit = 2

📍মানে আমরা A থেকে শুরু করে G খুঁজবো, কিন্তু সর্বোচ্চ ২ লেভেল পর্যন্তই যেতে পারবো।

found = depth_limited_search(start, goal, depth_limit)

if found:
    print(f"\n✅ '{goal}' found within depth {depth_limit}")
else:
    print(f"\n❌ '{goal}' NOT found within depth {depth_limit}")
 যদি found = True, তাহলে বলবে "G পাওয়া গেছে"
না হলে বলবে "G depth limit এর মধ্যে নেই"
