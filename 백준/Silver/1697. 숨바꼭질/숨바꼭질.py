from collections import deque

N, K = map(int, input().split())

MAX = 100000
visited = [-1] * (MAX + 1)

q = deque()
q.append(N)
visited[N] = 0

while q:
    cur = q.popleft()

    if cur == K:
        print(visited[cur])
        break

    for nxt in (cur - 1, cur + 1, cur * 2):
        if 0 <= nxt <= MAX and visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
