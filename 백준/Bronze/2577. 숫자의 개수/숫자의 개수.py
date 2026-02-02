a = int(input())
b = int(input())
c = int(input())

res = a * b * c
res = str(res)
list = [0]*10

for i in res:
    if i == '0':
        list[0] += 1
    elif i == '1':
        list[1] += 1
    elif i == '2':
        list[2] += 1
    elif i == '3':
        list[3] += 1
    elif i == '4':
        list[4] += 1
    elif i == '5':
        list[5] += 1
    elif i == '6':
        list[6] += 1
    elif i == '7':
        list[7] += 1
    elif i == '8':
        list[8] += 1
    elif i == '9':
        list[9] += 1

for i in list:
    print(i)