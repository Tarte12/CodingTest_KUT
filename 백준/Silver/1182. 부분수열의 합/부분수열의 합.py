n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum):
    global cnt
    if idx == n:
        if sum == s:
            cnt += 1
        return
    
    #1. 현재 숫자를 더할 때
    dfs(idx + 1, sum + lst[idx])
    #2. 현재 숫자를 안 더할 때
    dfs(idx + 1, sum)
dfs(0, 0)
if s == 0:
    cnt -= 1
    
print(cnt)