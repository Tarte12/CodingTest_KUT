numbers = list(map(int, input().split())) # 0~4까지 랜덤 수 5번에 검증수

sum = 0
# 검증수 구하기
for i in range(5):
    sum += numbers[i]*numbers[i]

num = sum % 10

print(num)