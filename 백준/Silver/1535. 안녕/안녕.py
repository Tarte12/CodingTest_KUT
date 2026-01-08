import sys
input = sys.stdin.readline
n = int(input())

lst1 = [0] + list(map(int, input().split())) #잃는 체력
lst2 = [0] + list(map(int, input().split())) #얻는 기쁨

res = [([0]*101) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if lst1[i] <= j: #잃는 체력이 남은 체력보다 작으면
            res[i][j] = max(res[i-1][j], res[i-1][j - lst1[i]] + lst2[i])
        else:
            res[i][j] = res[i - 1][j]


print(res[n][99])
