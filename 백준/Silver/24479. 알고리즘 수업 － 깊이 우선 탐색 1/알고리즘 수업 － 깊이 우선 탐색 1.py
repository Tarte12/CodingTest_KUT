import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
sol = [0] * (N+1)
count = 1  # 방문 순서 시작은 1

def dfs(v): 
    global count
    visited[v] = True
    sol[v] = count
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

dfs(R)

for i in range(1, N+1):
    print(sol[i])
