n = int(input())
count = {}

for _ in range(n):
    name = input()
    first = name[0] # 첫 글자

    count[first] = count.get(first, 0) + 1 
    #딕셔너리의 count(key, default) => 값이 있으면 key, 없으면 default 반환

res = []
for char in count:
    if count[char] >= 5:
        res.append(char)

if res:
    res.sort()
    print(''.join(res))
else:
    print("PREDAJA")