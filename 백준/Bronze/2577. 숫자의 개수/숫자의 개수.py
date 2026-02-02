a = int(input())
b = int(input())
c = int(input())

res = a * b * c
res = str(res)

for i in range(10):
    print(res.count(str(i)))