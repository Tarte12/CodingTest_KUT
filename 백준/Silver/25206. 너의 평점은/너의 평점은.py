# 과목명, 학점, 등급을 받는다
# 과목에 따라 과목 평점을 계산한다
# P/F에서 P는 제외
# 정답과의 절대오차 or 상대 오차 10^-4면 정답으로 인정
# 전공 평점 출력
# 전공 평점 = 학점 x 과목 평점
score = []
cnt = 0
for _ in range(20):
    a, b, c = input().split()
    b = float(b)

    cnt += b

    if c == 'A+':
        score.append(b*4.5)
    elif c == 'A0':
        score.append(b*4.0)
    elif c == 'B+':
        score.append(b*3.5)
    elif c == 'B0':
        score.append(b*3.0)
    elif c == 'C+':
        score.append(b*2.5)
    elif c == 'C0':
        score.append(b*2.0)
    elif c == 'D+':
        score.append(b*1.5)
    elif c == 'D0':
        score.append(b*1.0)
    elif c == 'F':
        score.append(b*0.0)
    else: #P일 땐 스킵
        cnt -= b
        continue

res = sum(score) / cnt
print(res)

