# 초기값
r = 31
m = 1234567891
res = 0

l = int(input())        # 문자열 길이
s = input()             # 문자열 입력

for i in range(l):
    value = ord(s[i]) - 96          # a=1, b=2 ... 변환
    res = (res + value * pow(r, i, m)) % m

print(res)
