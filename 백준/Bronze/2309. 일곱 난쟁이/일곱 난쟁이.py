import sys

height = [int(input()) for _ in range(9)]
total = sum(height)

for i in range(8):
    for j in range(i + 1, 9):
        if total - height[i] - height[j] == 100:
            result = [height[k] for k in range(9) if k != i and k != j]
            result.sort()  # 오름차순 출력 조건
            for x in result:
                print(x)
            sys.exit()
