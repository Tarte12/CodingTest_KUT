from collections import deque

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    
    # 처음부터 익은 토마토(1) 모두 큐에 넣기
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append((i, j))
    
    # BFS 시작
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 익지 않은 토마토(0)인 경우
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append((nx, ny))
    
    # 결과 계산
    max_day = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:  # 익지 않은 토마토가 남아있으면
                return -1
            max_day = max(max_day, tomato[i][j])
    
    # 처음부터 1이었으므로 -1 (0일부터 시작)
    return max_day - 1

# 입력
m, n = map(int, input().split())  # m: 가로(열), n: 세로(행)
tomato = [list(map(int, input().split())) for _ in range(n)]

# BFS 실행 및 출력
print(bfs())