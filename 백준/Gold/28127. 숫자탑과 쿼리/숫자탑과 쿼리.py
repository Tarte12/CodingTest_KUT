import sys
input = sys.stdin.readline

def cum(a, d, n):
    #등차수열의 합 - n층까지 누적된 블록 총개수 구하는 함수
    return a*n + d * (n-1)*n // 2

q = int(input().strip())
for _ in range(q):
    a, d, x = map(int, input().split())

    #이분 탐색 범위 설정
    lo, hi = 1, 2000000

    while lo < hi:
        mid = (lo + hi) // 2
        if cum(a, d, mid) < x:
            lo = mid + 1
        else:
            hi = mid

    layer = lo #lo가 x에 포함된 층

    #이전 층까지 누적 블럭 수
    prev_total = cum(a, d, layer - 1)

    #x가 해당 층에서 몇 번째인지
    position = x - prev_total

    print(layer, position)

