class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def compute_height(node):
    if not node.children:
        return 1
    heights = []
    for child in node.children:
        heights.append(compute_height(child))
    return 1 + max(heights)

n = int(input())
parents = list(map(int, input().split()))

# Create a list of nodes with values 0 to n-1
nodes = [Node(i) for i in range(n)]

# Connect child nodes to their parent nodes
for i, parent in enumerate(parents):
    if parent == -1:
        root = nodes[i]
    else:
        nodes[parent].children.append(nodes[i])

# Compute and output the height of the tree
print(compute_height(root))
