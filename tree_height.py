# python3

import sys
import threading
import numpy



def compute_height(n, parents):
    # create the tree as a list of lists
    tree = [[] for _ in range(n)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    
    # recursive function to compute the depth of a node
    def depth(node):
        if not tree[node]:
            return 1
        return 1 + max(depth(child) for child in tree[node])
    
    # compute the depth of the root node
    return depth(root)

def main():
    # read input
    n = int(input())
    parents = list(map(int, input().split()))
    
    # compute and print the height of the tree
    print(compute_height(n, parents))

# increase recursion limit and stack size for large trees
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
