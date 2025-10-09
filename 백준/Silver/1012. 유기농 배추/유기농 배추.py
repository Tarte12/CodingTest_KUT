from collections import deque

#입력 받는 조건
T = int(input())


#방향 리스트 => 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

#2차원부터는 좌표로 체크?
def bfs(x, y, N, M):
  queue = deque()
  queue.append((x, y))
  visited[y][x] = True #시작점 방문 처리

  while queue: 
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if not visited[ny][nx] and field[ny][nx] == 1:
          visited[ny][nx] = True
          queue.append((nx, ny))
  

#테스트 조건 만큼 체크해야 함
for _ in range(T):
  M, N, K = map(int, input().split())
  #배추밭 가로길이 M, 세로 길이 N, 배추 개수 K
  #배추밭 생성 + 아직 배추 없다고 생각하고 0으로 초기화
  field = [[0] * M for _ in range(N)]

  visited = [[False] * M for _ in range(N)]

  #베추 위치 <- K개
  for _ in range(K):
    x, y = map(int, input().split())
    #배추 좌표 입력
    field[y][x] = 1 #배추 심었음 -> 1인 부분만 배추라고 판단해야 하니까

  #인접한 배추 한 뭉치  => bfs 한 사이클
  #한 사이클 count => 배추흰지렁이 마릿수

  count = 0 #배추흰지렁이 마릿수

  for i in range(N):  # 세로줄 순회 (위에서 아래로)
   for j in range(M):  # 가로줄 순회 (왼→오)
      if field[i][j] == 1 and not visited[i][j]:
          bfs(j, i, M, N)  # bfs(x, y)
          count += 1  # 새로운 무더기 발견
  
  print(count)