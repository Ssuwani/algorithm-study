# 쇠막대기를 레이저로 절단
# 효율적으로 한번에 제거
# 쇠막대기의 양끝점은 겹치면 안된다.

# ()(((()())(())()))(())
# 3+3+3+2+1 + Start_cnt

seq = input()
seq = seq.replace("()", "l")
start = 0
result = 0


for s in seq:
    if s == "l":
        result += start
    elif s == "(":
        result += 1
        start += 1
    elif s == ")":
        start -= 1
print(result)
