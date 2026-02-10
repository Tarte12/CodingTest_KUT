num = int(input())
testnum = 0
SumOfComposition = False

while testnum < num:
    totsum = testnum
    for i in str(testnum):
        totsum += int(i)
    if totsum == num:
        SumOfComposition = True
        break
    testnum += 1

if SumOfComposition:
    print(testnum)
else:
    print(0)