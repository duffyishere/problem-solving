import sys


input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 0x3f3f3f3f
adj = [list(INF for _ in range(n + 1)) for _ in range(n + 1)]

for _ in range(m):
    i, j, c = map(int, input().split())
    adj[i][j] = min(adj[i][j], c)

for i in range(1, n + 1):
    adj[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i in range(1, n + 1):
    result = []
    for j in range(1, n + 1):
        if adj[i][j] == INF:
            result.append(0)
        else:
            result.append(adj[i][j])
    print(*result)