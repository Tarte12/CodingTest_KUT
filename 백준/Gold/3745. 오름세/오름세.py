import sys
from bisect import bisect_left

input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break

    n = int(line)
    arr = list(map(int, input().split()))

    dp = []

    for x in arr:
        idx = bisect_left(dp, x)
        if idx == len(dp):
            dp.append(x)
        else:
            dp[idx] = x

    print(len(dp))
