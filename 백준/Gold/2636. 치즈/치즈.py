from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def bfs_air():
    """외부 공기(0)가 퍼지는 영역을 BFS로 체크하고,
    그 과정에서 치즈(1)와 맞닿은 부분을 찾아 녹일 후보에 저장"""
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    melt = []  # 이번 턴에 녹을 치즈 좌표들

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True

                if board[nx][ny] == 0:
                    q.append((nx, ny))
                elif board[nx][ny] == 1:
                    melt.append((nx, ny))

    return melt


time = 0          # 총 걸린 시간
last_melt = 0     # 마지막에 녹은 치즈 개수

while True:
    melt_list = bfs_air()

    if not melt_list:
        # 더 이상 녹을 치즈가 없다 → 종료
        print(time)
        print(last_melt)
        break

    # melt_list의 치즈들을 녹인다
    last_melt = len(melt_list)
    for x, y in melt_list:
        board[x][y] = 0

    time += 1
