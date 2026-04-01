import bisect
import heapq
import sys


input = sys.stdin.readline
n, k = map(int, input().split())
crystal = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
crystal.sort(key=lambda x: x[0])
bags.sort()

heap = []
result = 0
idx = 0

for bag in bags:
    while idx < n and crystal[idx][0] <= bag:
        heapq.heappush(heap, -crystal[idx][1])
        idx += 1

    if heap:
        result += -heapq.heappop(heap)

print(result)