from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    union = [(x, y)]
    population_sum = board[x][y]

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[cx][cy] - board[nx][ny]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    population_sum += board[nx][ny]

    return union, population_sum


days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, pop_sum = bfs(i, j, visited)

                if len(union) > 1:
                    moved = True
                    new_pop = pop_sum // len(union)
                    for x, y in union:
                        board[x][y] = new_pop

    if not moved:
        break

    days += 1

print(days)
