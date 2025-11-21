n, m = map(int, input().split())

maze = []

for _ in range(n):
	candy = list(map(int, input().split()))
	row = [0] + candy
	maze.append(row)

zero_row = [0] * (m+1)
maze.insert(0, zero_row)

dp = []
for _ in range(n+1):
	row = [0]* (m+1)
	dp.append(row)

dp[1][1] = maze[1][1]

for j in range(2, m+1):
	dp[1][j] = maze[1][j] + dp[1][j-1]
	#1행은 왼쪽에만 올 수 있음

for i in range(2, n+1):
	dp[i][1] = maze[i][1] + dp[i-1][1]
	#1열은 위에서만 올 수 있음

#나머지는 점화식으로 넣어서 값 채우기
for i in range(2,n+1):
	for j in range(2, m+1):
		dp[i][j] = maze[i][j] #현재값 넣고
		dp[i][j] += max(dp[i-1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[n][m])