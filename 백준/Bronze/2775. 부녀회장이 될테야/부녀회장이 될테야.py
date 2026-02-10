t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    #dp[k층][n호] 배열 생성 (0층~k층, 1호~n호)
    dp = [[0] * (n+1) for _ in range(k+1)]

    # 0층 초기화
    for i in range(1, n+1):
        dp[0][i] = i

    #1층부터 k층까지 계산
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[k][n])