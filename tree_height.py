# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    tree = {}
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(i)
    return get_height(tree, root)

def get_height(tree, root):
    if root not in tree:
        return 1
    max_height = 0
    for child in tree[root]:
        height = get_height(tree, child)
        max_height = max(max_height, height)
    return max_height + 1


def main():
    # read input
    n = int(input())
    parents = list(map(int, input().split()))

    # compute height of the tree
    height = compute_height(n, parents)

    # write output
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
