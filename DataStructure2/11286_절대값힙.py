import heapq
import sys

input = sys.stdin.readline
heap = []

n = int(input())


for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, (abs(num), num))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)
