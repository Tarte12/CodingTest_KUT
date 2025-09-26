from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heap = scoville[:]           # 원본 보존
    heapify(heap)                # 제자리 힙 변환 (반환값 없음)
    answer = 0

    # 최솟값이 K 이상이면 끝
    while heap and heap[0] < K:
        if len(heap) == 1:       # 두 개 미만이면 더 못 섞음
            return -1
        a = heappop(heap)        # 가장 약한 두 개
        b = heappop(heap)
        heappush(heap, a + 2*b)  # 새 스코빌 푸시
        answer += 1

    return answer
