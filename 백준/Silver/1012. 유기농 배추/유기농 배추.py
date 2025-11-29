from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):      # (x,y): (가로,세로)
    que = deque()
    que.append((x, y))
    visited[y][x] = True   # (y,x)

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크 (x는 가로, y는 세로)
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and map_lst[ny][nx] == 1:
                    visited[ny][nx] = True
                    que.append((nx, ny))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())  # m=가로, n=세로

    # map[y][x] 형태로 생성
    map_lst = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())  # (x:가로, y:세로)
        map_lst[y][x] = 1

    cnt = 0
    for y in range(n):        # 세로 먼저
        for x in range(m):    # 가로
            if map_lst[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                cnt += 1

    print(cnt)
