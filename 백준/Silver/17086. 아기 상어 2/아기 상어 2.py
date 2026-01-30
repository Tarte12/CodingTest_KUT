from collections import deque

n, m = map(int, input().split())

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

visited = [[False] * m for _ in range(n)]
graph = []
queue = deque()

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j, 0))  # 거리 추가!

result = 0

while queue:
    x, y, dist = queue.popleft()

    if visited[x][y]:
        continue
    visited[x][y] = True
    result = max(result, dist)

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:  # 들여쓰기 확인!
            queue.append((nx, ny, dist + 1))

print(result)