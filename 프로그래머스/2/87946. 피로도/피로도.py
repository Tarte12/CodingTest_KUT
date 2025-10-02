def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0

    def dfs(energy, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and energy >= need:  # 아직 안 갔고 조건 만족
                visited[i] = True
                dfs(energy - cost, count + 1)
                visited[i] = False  # 백트래킹

    dfs(k, 0)
    return answer
