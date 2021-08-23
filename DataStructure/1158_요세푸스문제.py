n, k = map(int, input().split())
step = 0
result = []
seq = list(range(1, n+1))
for i in range(n):
    step += k - 1
    if len(seq) < step+1:
        step %= len(seq)
    result.append(seq.pop(step))

print(str(result).replace('[', '<').replace(']', '>'))