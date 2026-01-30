def solution(money):
    ans = 0
    n = len(money)
    
    if n == 1:
        return money[0]
    if n == 2 or n == 3:
        return max(money)
    
    # dp 함수
    def rob(start, end):
        dp = [0]*(n+1)
    
        for i in range(start, end):
            #i번째 집 터는 경우(i-1은 털면 안 됨) or 털지 않는 경우 (i-1을 털어야 됨)
            dp[i] = max(dp[i-2] + money[i], dp[i-1])
        return dp[end-1]

    ans = max(rob(0, n-1), rob(1, n))

    return ans