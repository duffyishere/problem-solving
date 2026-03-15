import sys


input = sys.stdin.readline
n = int(input())
logs = dict()
for _ in range(n):
    name, status = input().split()
    if name in logs:
        logs.pop(name)
    else:
        logs[name] = True

result = list(logs.keys())
result.sort(reverse=True)
for r in result:
    print(r)