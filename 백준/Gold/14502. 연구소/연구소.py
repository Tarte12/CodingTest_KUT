from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

empties = []  # 빈 칸(벽 후보)
virus = []    # 바이러스 위치

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            empties.append((x, y))
        elif graph[y][x] == 2:
            virus.append((x, y))

answer = 0
L = len(empties)

def bfs():
    temp = [row[:] for row in graph]   # list slicing → deepcopy보다 훨씬 빠름
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 2
                    q.append((nx, ny))

    safe = 0
    for y in range(n):
        for x in range(m):
            if temp[y][x] == 0:
                safe += 1

    return safe


def build_wall(start, count):
    global answer

    if count == 3:
        answer = max(answer, bfs())
        return

    # empties 배열에서 index 증가만 허용 → 조합 중복 없음
    for i in range(start, L):
        x, y = empties[i]
        if graph[y][x] == 0:
            graph[y][x] = 1
            build_wall(i + 1, count + 1)
            graph[y][x] = 0


build_wall(0, 0)
print(answer)
