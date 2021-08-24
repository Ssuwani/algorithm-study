from collections import deque
import sys

input = sys.stdin.readline
q = deque([])

for _ in range(int(input())):
    cs = input().split()
    if cs[0] == 'push_back':
        q.appendleft(cs[1])
    elif cs[0] == 'push_front':
        q.append(cs[1])
    elif cs[0] == 'front':
        print(q[-1] if q else -1)
    elif cs[0] == 'back':
        print(q[0] if q else -1)
    elif cs[0] == 'size':
        print(len(q))
    elif cs[0] == 'empty':
        print(1 if not q else 0)
    elif cs[0] == 'pop_front':
        print(q.pop() if q else -1)
    elif cs[0] == 'pop_back':
        print(q.popleft() if q else -1)
    