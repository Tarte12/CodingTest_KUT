from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = max(map(max, graph))

def bfs(x, y, height, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 물에 잠기지 않고 아직 방문하지 않은 지역만 이동
                if not visited[nx][ny] and graph[nx][ny] > height:
                    visited[nx][ny] = True
                    q.append((nx, ny))


answer = 1  # 아무 지역도 잠기지 않는 경우(비가 안 옴)

for h in range(1, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    safe_count = 0

    for i in range(n):
        for j in range(n):
            # h보다 큰 지역(= 물에 잠기지 않음)이고 방문 안 했으면 BFS 시작
            if graph[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited)
                safe_count += 1

    answer = max(answer, safe_count)

print(answer)
