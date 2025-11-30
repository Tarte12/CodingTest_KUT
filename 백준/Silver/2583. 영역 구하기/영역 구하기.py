from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
	que = deque()
	que.append((x, y))
	visited[y][x] = True
	area = 1

	while que:
		x, y = que.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < m and 0 <= ny < n:
				if not visited[ny][nx] and map_lst[ny][nx] ==1:
					visited[ny][nx] = True
					area += 1
					que.append((nx, ny))
	return area

n, m, k = map(int, input().split())

areas = []

map_lst = [[1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for _ in range(k):
	x1, y1, x2, y2 = map(int, input().split())
	
	for i in range(y1, y2):
		for j in range(x1, x2):
				map_lst[i][j] = 0

cnt = 0
for y in range(n):
	for x in range(m):
		if map_lst[y][x] and not visited[y][x]:
			area_size = bfs(x, y)
			areas.append(area_size)

areas.sort()
print(len(areas))
print(*areas)
