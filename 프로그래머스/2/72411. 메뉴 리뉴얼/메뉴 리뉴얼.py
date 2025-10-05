from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for num in course:
        freq = Counter()  # num 길이 조합 빈도표

        for order in orders:
            if len(order) < num:
                continue
            s = ''.join(sorted(order))                     # 'BA' == 'AB'로 맞추기
            freq.update(''.join(c) for c in combinations(s, num))  # 리스트 안 만들고 바로 집계

        if not freq:
            continue
        mx = max(freq.values())
        if mx < 2:                                        # 최소 2명 조건
            continue

        # 동률 전부 채택
        answer.extend([menu for menu, cnt in freq.items() if cnt == mx])

    return sorted(answer)                                 # 최종 사전순 정렬
