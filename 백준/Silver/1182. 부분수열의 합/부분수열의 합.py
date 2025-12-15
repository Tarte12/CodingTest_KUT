from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for r in range(1, n + 1):        # 공집합 제외
    for comb in combinations(nums, r):
        if sum(comb) == s:
            cnt += 1

print(cnt)