a, b, v = map(int, input().split())

if a >= v:
    print(1)
else: 
    days = (v - a + (a - b) - 1) // (a - b)
    print(days + 1)