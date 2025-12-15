from itertools import combinations

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

people = list(range(n))
half = n // 2
min_diff = float('inf')

# 1️⃣ 팀 A 조합 선택
for team_a in combinations(people, half):
    team_b = [p for p in people if p not in team_a]

    score_a = 0
    score_b = 0

    # 2️⃣ 팀 A 능력치 계산
    for i in range(half):
        for j in range(i + 1, half):
            a1, a2 = team_a[i], team_a[j]
            score_a += S[a1][a2] + S[a2][a1]

    # 3️⃣ 팀 B 능력치 계산
    for i in range(half):
        for j in range(i + 1, half):
            b1, b2 = team_b[i], team_b[j]
            score_b += S[b1][b2] + S[b2][b1]

    # 4️⃣ 차이 갱신
    min_diff = min(min_diff, abs(score_a - score_b))

print(min_diff)
