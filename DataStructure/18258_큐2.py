from collections import deque
from sys import stdin

n = int(input())

q = deque()

for _ in range(n):
    cs = stdin.readline().rstrip().split()
    if cs[0] == "push":
        q.append(cs[1])
    elif cs[0] == "front":
        print(q[0] if q else -1)
    elif cs[0] == "back":
        print(q[-1] if q else -1)
    elif cs[0] == "size":
        print(len(q))
    elif cs[0] == "empty":
        print(0 if q else 1)
    elif cs[0] == "pop":
        print(q.popleft() if q else -1)
