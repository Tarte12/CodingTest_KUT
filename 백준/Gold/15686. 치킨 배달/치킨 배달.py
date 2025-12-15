from itertools import combinations

n, m = map(int, input().split())  # n=도시 크기, m=살릴 치킨집 수
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
min_res = float('inf')

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

for chi in combinations(chicken, m):  # 치킨집 m개 선택
    city_dist = 0

    for hx, hy in house:  # 각 집마다
        min_dist = float('inf')

        for cx, cy in chi:  # 선택된 치킨집 중에서만 최소 거리
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)

        city_dist += min_dist  # 도시 치킨 거리 누적

    min_res = min(min_res, city_dist)

print(min_res)
