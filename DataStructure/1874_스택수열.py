import sys

input = sys.stdin.readline

n = int(input())
seq = []
state = 0
boxes = []
for _ in range(n):
    m = int(input())

    seq += list(range(state + 1, m + 1))
    boxes += ["+"] * (m - state)
    if seq[-1] == m:
        seq.pop()
        boxes.append("-")
    else:
        boxes = []
        break
    state = max(state, m)
print("\n".join(boxes)) if boxes else print("NO")
