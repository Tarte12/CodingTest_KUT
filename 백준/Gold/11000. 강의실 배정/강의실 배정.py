import heapq
import sys
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
#times = [(s1, t1), (s2, t2), (s3, t3)...]
answer = 0
times.sort()
heap = [] #진행 중 강의들의 종료 시간

for s, e in times: #times는 배정되어야 하므로 다 돌아야 해
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    answer = max(answer, len(heap))
print(answer)


           
