#bfs밖 -> 게임 전체에서 유지되어야 하는 것
#bfs안 -> 한 번의 탐색마다 새로 시작해야 하는 것
#큐에서 꺼낸 현재 위치 정보
from collections import deque

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

# 상어 초기 위치 찾기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            shark_x, shark_y = i, j
            grid[i][j] = 0  # 시작 위치도 0으로

time = 0 #시간 체크
size = 2 #상어 사이즈 체크
cnt = 0 #몸집 키우는 거 카운트

dx = [-1, 0, 0, 1]  # 상 좌 우 하 (문제 조건: 위→왼쪽 우선)
dy = [0, -1, 1, 0]


def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    fish = [] #먹을 물고기 후보군 좌표 리스트

    while queue:
        cx, cy, dist = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] <= size:  # 지나갈 수 있음
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

                    if 0 < grid[nx][ny] < size:  # 먹을 수 있음
                        fish.append((dist + 1, nx, ny))

    return fish


while True:
    fish = bfs(shark_x, shark_y)

    if not fish:  # 먹을 물고기 없으면 종료
        break

    fish.sort()  # (거리, x, y) 순으로 정렬 → 조건 만족
    dist, shark_x, shark_y = fish[0]

    time += dist
    grid[shark_x][shark_y] = 0  # 물고기 먹음
    cnt += 1

    if cnt == size:  # 크기만큼 먹으면 성장
        size += 1
        cnt = 0

print(time)