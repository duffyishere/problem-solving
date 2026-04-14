import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def a():
    t = int(sys_input())
    for _ in range(t):
        n = int(sys_input())
        arr = list(map(int, sys_input().split()))
        arr.sort(reverse=True)
        if len(set(arr)) != n:
            print(-1)
        else:
            print(*arr)


def b():
    t = int(sys_input())
    for _ in range(t):
        n, m = map(int, sys_input().split())
        arr = list(map(int, sys_input().split()))

        seq_cnt = 1
        ok = True
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                seq_cnt += 1
                if m <= seq_cnt:
                    ok = False
                    break
            else:
                seq_cnt = 1

        print("YES" if ok else "NO")
