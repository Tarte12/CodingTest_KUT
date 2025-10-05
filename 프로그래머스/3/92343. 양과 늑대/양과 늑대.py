from collections import deque
import sys
sys.setrecursionlimit(10**6)

def solution(info, edges):
    # 1) 그래프 구성
    n = len(info)
    graph = [[] for _ in range(n)]
    for parent, child in edges:
        graph[parent].append(child)

    answer = 0

    # 2) DFS: 후보 집합 기반
    def dfs(sheep, wolf, candidates, taken_mask):
        nonlocal answer
        # 현재 양 수로 정답 후보 갱신
        if sheep > answer:
            answer = sheep

        # 후보가 없으면 끝
        if not candidates:
            return

        # 후보 중 하나를 선택해서 진행
        for node in list(candidates):
            # 다음 상태 계산
            ns, nw = sheep, wolf
            if info[node] == 0:
                ns += 1
            else:
                nw += 1

            # 가지치기: 늑대가 양 이상이면 진행 불가
            if ns <= nw:
                continue

            # 다음 후보 집합 만들기
            next_candidates = set(candidates)
            next_candidates.remove(node)
            # node의 자식들을 후보에 추가
            for child in graph[node]:
                if not (taken_mask & (1 << child)):  # 이미 뽑은 노드는 제외
                    next_candidates.add(child)

            # 방문 마스크 갱신
            next_mask = taken_mask | (1 << node)

            # [선택] 메모이제이션/가지치기 추가할 자리 (TODO)
            # ex) seen[(next_mask, ns, nw)] 등으로 상태 컷

            dfs(ns, nw, next_candidates, next_mask)

    # 3) 시작 상태 설정
    # 후보: {0}, 아직 어떤 노드도 뽑지 않음
    start_candidates = {0}
    start_mask = 0

    # 보통은 0을 후보로 둔 뒤, 재귀 안에서 0을 '선택'하는 흐름으로 통일
    dfs(0, 0, start_candidates, start_mask)

    return answer
