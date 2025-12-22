from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]

INF = 10**9
dist = [[INF]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((0, 0))
dist[0][0] = 0

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            cost = dist[x][y]

            # 흰 방(1): 비용 0
            if board[nx][ny] == 1:
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    dq.appendleft((nx, ny))

            # 검은 방(0): 비용 1
            else:
                if dist[nx][ny] > cost + 1:
                    dist[nx][ny] = cost + 1
                    dq.append((nx, ny))

print(dist[n-1][n-1])
