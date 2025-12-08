from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())

# 맵 입력
map_lst = [list(input().strip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    sheep = 0
    wolf = 0

    # 현재 위치에 양/늑대가 있는지 체크
    if map_lst[x][y] == 'o':
        sheep += 1
    elif map_lst[x][y] == 'v':
        wolf += 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                # 벽은 통과 불가
                if map_lst[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                    if map_lst[nx][ny] == 'o':
                        sheep += 1
                    elif map_lst[nx][ny] == 'v':
                        wolf += 1

    # 한 영역 끝난 후 생존 판정
    return sheep, wolf


total_sheep = 0
total_wolf = 0

# 전체 탐색
for i in range(r):
    for j in range(c):
        if not visited[i][j] and map_lst[i][j] != '#':
            s, w = bfs(i, j)

            if s > w:
                total_sheep += s
            else:
                total_wolf += w

print(total_sheep, total_wolf)
