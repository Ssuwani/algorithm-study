n, m = map(int, input().split())

strings = [input() for _ in range(n)]

print(sum([input() in strings for _ in range(m)]))
    