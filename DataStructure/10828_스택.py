from sys import stdin


n = int(input())

stack = []
for _ in range(n):
    cs = stdin.readline().rstrip().split()
    if cs[0] == 'push':
        stack.append(cs[1])
    elif cs[0] == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif cs[0] == 'size':
        print(len(stack))
    elif cs[0] == 'empty':
        print(0) if stack else print(1)
    elif cs[0] == 'top':
        print("topiii")
        print(stack[-1]) if stack else print(-1)
