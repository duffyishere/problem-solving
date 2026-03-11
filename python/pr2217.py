import sys


input = sys.stdin.readline
n = int(input())
ropes = sorted([int(input().rstrip()) for _ in range(n)])
result = 0
for i in range(0, len(ropes)):
    result = max(result, ropes[i] * (len(ropes) - i))

print(result)