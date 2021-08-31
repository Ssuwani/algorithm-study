import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

dict_m = {}
dict_r = {}
for i in range(1, n+1):
    name = input().strip()

    dict_m[name] = i
    dict_r[i] = name

for j in range(m):
    name = input().strip()

    if name.isdigit():
        print(dict_r[int(name)])
    else:
        print(dict_m[name])