from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 1단계: 섬 번호 매기기
island = [[0] * N for _ in range(N)]
island_id = 0

def label_island(x, y, idx):
    q = deque([(x, y)])
    island[x][y] = idx

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1 and island[nx][ny] == 0:
                    island[nx][ny] = idx
                    q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and island[i][j] == 0:
            island_id += 1
            label_island(i, j, island_id)

# 2단계: 다리 만들기 (BFS 확장)
def build_bridge(idx):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if island[i][j] == idx:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if island[nx][ny] != 0 and island[nx][ny] != idx:
                    return dist[x][y]
                if island[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return float('inf')

answer = float('inf')
for i in range(1, island_id + 1):
    answer = min(answer, build_bridge(i))

print(answer)
