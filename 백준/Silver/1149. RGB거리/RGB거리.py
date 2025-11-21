n = int(input())

# 빨강(r) 초록(g) 파랑(b)을 칠할 때 비용 발생
# 서로 이웃한 집은 같은 색 불가

cost = []
for _ in range(n):
	row = list(map(int, input().split()))
	cost.append(row)

dp = []
for _ in range(n):
	dp.append([0, 0, 0])

dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, n):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))