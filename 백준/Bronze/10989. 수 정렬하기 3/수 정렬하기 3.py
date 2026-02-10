import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
counts = [0] * 10001  # 1~10000 범위

for _ in range(n):
    counts[int(input())] += 1

for num in range(1, 10001):
    for _ in range(counts[num]):
        write(f"{num}\n")
