from collections import deque

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

res = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            res.append(bfs(i, j))

res.sort()
print(len(res))
for x in res:
    print(x)
