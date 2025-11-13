from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    distance[x][y] = 1  # 시작점의 거리는 1
    
    while queue:
        x, y = queue.popleft()
        
        # 목적지에 도착하면 거리 반환
        if x == n-1 and y == m-1:
            return distance[x][y]
        
        for i in range(4):  # 콜론 추가
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if distance[nx][ny] == 0 and miro[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    
    return distance[n-1][m-1]

# 입력 받기
n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]  # 공백 없이 입력받음
distance = [[0] * m for _ in range(n)]

# BFS 실행 (0, 0)부터 시작
result = bfs(0, 0)
print(result)