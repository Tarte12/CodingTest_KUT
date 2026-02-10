num = list(map(int, input().split()))

num_sort = sorted(num)
num_reverse = sorted(num, reverse=True)

if num == num_sort:
    print("ascending")
elif num == num_reverse:
    print("descending")
else:
    print("mixed")