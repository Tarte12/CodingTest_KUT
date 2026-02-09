import sys
import heapq

def solve():
    # 빠른 입력을 위한 설정
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    # 몬스터별 기본 난이도 (1-based index)
    c = [0] + list(map(int, input().split()))
    
    P = int(input())
    
    # influence[a] = [(b, d), ...] -> a를 안 잡으면 b 잡을 때 d만큼 난이도 증가
    influence = [[] for _ in range(N + 1)]
    # 몬스터 b를 잡을 때, 몬스터 a가 아직 잡히지 않았다면 난이도 증가
    # 역방향 영향을 저장해야 함. 즉, a가 잡혔을 때 b의 난이도가 감소
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(P):
        a, b, d = map(int, input().split())
        c[b] += d # 초기에는 a를 안 잡았다고 가정하고 난이도 추가
        adj[a].append((b, d)) # a가 잡히면 b의 난이도가 줄어듦

    # 몬스터가 잡혔는지 확인하는 배열
    visited = [False] * (N + 1)
    # (현재 몬스터 난이도, 몬스터 번호)
    pq = []
    
    for i in range(1, N + 1):
        heapq.heappush(pq, (c[i], i))
        
    cnt = 0
    max_diff = 0
    
    while pq and cnt < M:
        diff, cur = heapq.heappop(pq)
        
        if visited[cur]:
            continue
        
        visited[cur] = True
        cnt += 1
        max_diff = max(max_diff, diff)
        
        # 몬스터 cur를 잡음 -> cur에 의해 난이도가 증가했던 다른 몬스터들의 난이도 감소
        for next_mon, d in adj[cur]:
            if not visited[next_mon]:
                c[next_mon] -= d
                heapq.heappush(pq, (c[next_mon], next_mon))
                
    print(max_diff)

solve()
