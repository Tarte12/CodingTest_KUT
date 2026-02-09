import sys

def solve():
    input = sys.stdin.read().split()
    N = int(input[0])
    M = int(input[1])
    
    # 갈 수 없는 돌 체크
    bad_stones = set(map(int, input[2:]))
    
    # 최대 속도 설정 (약 sqrt(2N))
    max_v = int((2 * N)**0.5) + 1
    
    # DP 테이블 초기화 (충분히 큰 값으로)
    dp = [[float('inf')] * (max_v + 1) for _ in range(N + 1)]
    
    # 시작점: 1번에서 2번으로 점프 (속도 1, 횟수 1)
    if 2 not in bad_stones:
        dp[2][1] = 1
    
    for i in range(2, N + 1):
        for v in range(1, max_v):
            if dp[i][v] == float('inf'):
                continue
            
            # 가속(v+1), 유지(v), 감속(v-1) 세 가지 경우 탐색
            for dv in [v-1, v, v+1]:
                if dv > 0:
                    next_stone = i + dv
                    if next_stone <= N and next_stone not in bad_stones:
                        dp[next_stone][dv] = min(dp[next_stone][dv], dp[i][v] + 1)
    
    result = min(dp[N])
    print(result if result != float('inf') else -1)

solve()
