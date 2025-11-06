from collections import deque
#BFS 쓸 거니까 일단 붙이고

def bfs(v):
  global count #웜 바이러스 카운팅
  queue = deque([v])
  visited[v] = True #여긴 1번 컴퓨터라 카운팅 x
  while queue:
    v = queue.popleft()
    for i in com_graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True #큐에 넣을 때 방문 체크
        count += 1


com = int(input()) #컴퓨터의 수(정점 수)
com_net = int(input()) #연결된 컴퓨터 쌍의 수(간선 수)


com_graph = [[] for _ in range(com+1)] #컴퓨터 수 만큼 인접 리스트 생성

for i in range(com_net): #이어진 간선 수 만큼 반복
  #여기에서 인접 리스트 만들어야 함
  a, b = map(int, input().split()) #연결된 컴퓨터 쌍 입력
  com_graph[a].append(b)
  com_graph[b].append(a)

#무조건 1번 컴퓨터가 웜바이러스라 1번 컴퓨터가 V
#연결되어 있으면 다 웜바이러스 
#한 사이클 내에 있으면 다 웜바이러스

visited = [False]*(com+1) #방문 여부 체크
count = 0

bfs(1)
print(count)
