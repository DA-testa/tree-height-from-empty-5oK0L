import sys
import threading


def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def compute_depth(node):
        if not tree[node]:
            return 1
        max_height = 0
        for children in tree[node]:
            depth = compute_depth(children)
            max_height = max(max_height, depth)
        return max_height + 1

    return compute_depth(root)


def main():
    input_type = input()

    if 'I' in input_type:
        m = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(m, parents)
        print(height)
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as f:
            m = int(f.readline())
            parents = list(map(int, f.readline().split()))
            height = compute_height(m, parents)
            print(height)
    else:
        print("error")
        exit()


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
