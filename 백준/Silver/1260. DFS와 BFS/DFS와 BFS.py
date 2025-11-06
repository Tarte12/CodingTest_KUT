#파이썬은 양방향 큐인 deque를 사용
from collections import deque

#정점 갯수 N, 간선 갯수 M, 탐색 시작 정점 번호 V
N, M, V = map(int, input().split())

#DFS -> Stack or 재귀함수

visited = [False] * (N + 1)
#방문 안 한 기본값이 False
#방문해야 하는 정점 갯수 만큼 길이

sol_dfs = []


def dfs(v):
  visited[v] = True  #v를 true로 바꿔서 방문 처리
  sol_dfs.append(v)
  for i in graph[v]:  #그래프 전체를 순회하겠다
    if not visited[i]:  #방문 처리가 안 된 곳이면
      dfs(i)  #재귀함수 호출


#BFS -> Queue
sol_bfs = []


#리스트를 이용해서 큐를 만들 수 있지만
#pop(0) 연산이 O(N)만큼 걸리기 때문에 느려서 그냥
#deque 사용하는 게 나음 (양방향 큐)
#list.pop(0) => O(N)
#deque.popleft() => O(1)
def bfs(v):
  queue = deque()  #큐 생성
  queue = deque([v])  #시작 정점을 큐에 삽입
  visited[v] = True  #여기까진 방문 처리라 dfs랑 동일

  while queue:  #큐가 빌 때까지 반복
    v = queue.popleft()  #큐에서 원소 하나 뽑아내기
    sol_bfs.append(v)
    #이미 위에서 시작점을 방문 처리 했기 때문에 빼야 함
    for i in graph[v]:  #그래프 전체를 순회하겠다
      if not visited[i]:  #방문 처리가 안 된 곳이면
        queue.append(i)  #큐에 넣어주기
        visited[i] = True


#그래프 => 인접 리스트 아이디어
# (N+1)만큼 만들어서 정점 갯수만큼 리스트를 만들고
# 이 내용을 다 모은 리스트를 만들어서 그래프라고 하겠
graph = [[] for _ in range(N + 1)]

for i in range(M):
  #간선 정보 <- 간선이 연결한 정점의 번호
  #a 정점의 인접한 정점으로 b를 넣겠다
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)  #무방향 그래프만
#여기까지 그래프 생성 완료
for i in range(1, N + 1):
  graph[i].sort()

#그러면 이걸 탐색하는 게 DFS/BFS
#위에서 함수를 정의하고 아래에서 호출

dfs(V)  #위에서 시작하기로 한 V에서 시작하는 dfs 호출
visited = [False] * (N + 1)  #초기화
bfs(V)  #위에서 시작하기로 한 V에서 시작하는 bfs 호출
print(*sol_dfs)
print(*sol_bfs)

