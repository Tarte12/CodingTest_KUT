t = int(input())

for i in range(t):
    str = input()
    streak = 0
    score = 0

    for ch in str:
        if ch == "O":
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)