def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

t = int(input())

for _ in range(t):
    s = input()
    l, r = 0, len(s) - 1
    answer = 0

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if is_pal(s, l+1, r) or is_pal(s, l, r-1):
                answer = 1
            else:
                answer = 2
            break

    print(answer)