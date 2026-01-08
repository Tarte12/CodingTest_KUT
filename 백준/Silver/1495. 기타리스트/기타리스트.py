import sys
input = sys.stdin.readline

n, s, max_v = map(int, input().split())
v_lst = list(map(int, input().split()))

dp = []
for _ in range(n+1):
    dp.append([False] * (max_v + 1))

dp[0][s] = True

for i in range(n):
    for j in range(max_v + 1):
        if dp[i][j]:
            if j + v_lst[i] <= max_v:
                dp[i+1][j + v_lst[i]] = True
            if j - v_lst[i] >= 0:
                dp[i+1][j - v_lst[i]] = True

res = -1
for i in range(max_v + 1):
    if dp[n][i]:
        res = i

print(res)
