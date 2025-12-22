from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1]*m for _ in range(n)]
q = deque()

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i, j))
            dist[i][j] = 0
        elif graph[i][j] == 0:
            dist[i][j] = 0   # 갈 수 없는 곳은 0 유지

# BFS
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

# 출력
for row in dist:
    print(*row)
