def minimax(node, depth, maximizingPlayer, alpha, beta):
    # যদি leaf node বা নির্দিষ্ট গভীরে পৌঁছায়
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in get_children(node):
            eval = minimax(child, depth-1, False, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # prune
        return maxEval
    else:
        minEval = float('inf')
        for child in get_children(node):
            eval = minimax(child, depth-1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # prune
        return minEval


# Helper functions (তুই নিজের মতো করে লিখবি)
def is_terminal(node):
    # node কি leaf? (যেমন খেল শেষ হয়েছে)
    pass

def evaluate(node):
    # node এর value/score ক্যালকুলেট করা
    pass

def get_children(node):
    # node থেকে possible next moves (child nodes) রিটার্ন করবে
    pass


.....................code analysis.................

def minimax(node, depth, maximizingPlayer, alpha, beta):
    # যদি leaf node বা নির্দিষ্ট গভীরে পৌঁছায়
    if depth == 0 or is_terminal(node):
        return evaluate(node)
এখানে চেক করছি, যদি depth == 0 অর্থাৎ আমরা নির্দিষ্ট গভীরে পৌঁছেছি (search শেষ) বা গেম শেষ হয়েছে (leaf node), তাহলে আমরা ঐ node এর মান (score) রিটার্ন করব।
................
    if maximizingPlayer:
        maxEval = float('-inf')

যদি আমরা maximizer player (মানে যিনি score বাড়াতে চান), তাহলে শুরুতে maxEval কে খুব ছোট একটা মান দিয়ে initialize করছি (−∞), যাতে নতুন পাওয়া যেকোন মান বড় মনে হবে।
.................
        for child in get_children(node):

এখন ঐ node থেকে সব possible পরবর্তী অবস্থান বা move (child nodes) নিয়ে লুপ চালাচ্ছি।
.............................
            eval = minimax(child, depth-1, False, alpha, beta)
প্রত্যেক child node এর জন্য minimax ফাংশন recursive কল করছি।

depth-1 করা কারণ এক লেভেল নিচে যাচ্ছি।

এখানে False দিলাম, কারণ এখন opponent এর পালা (minimizing player)।
..............................
            maxEval = max(maxEval, eval)
আমরা এখন পর্যন্ত পাওয়া সর্বোচ্চ মানকে update করছি।
...................
            alpha = max(alpha, eval)
alpha হলো maximizer এর জন্য সর্বোচ্চ নিশ্চিত মান। এটা আপডেট করছি, কারণ আমরা নতুন কোনো বড় মান পেয়েছি।
......................
            if beta <= alpha:
                break  # prune
যদি beta (minimizer এর সর্বনিম্ন মান) ছোট বা সমান alpha হয়ে যায়, তাহলে আর নিচের branch গুলো চেক করার দরকার নেই — pruning করা হচ্ছে।
