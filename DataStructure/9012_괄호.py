n = int(input())

for _ in range(n):
    s = input()
    while "()" in s:
        s = s.replace("()", "")
    print("NO" if s else "YES")
