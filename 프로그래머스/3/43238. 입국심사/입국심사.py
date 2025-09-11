def solution(n, times):
    answer = 0
    lt = 1
    rt = max(times)*n
    while lt <= rt:
        mid = (lt + rt) // 2 #mid 시간 안에 몇 명 처리?
        total = sum(mid // time for time in times)
        
        if total >= n: #mid 시간 내에 n명 이상 처리 가능
            answer = mid
            rt = mid - 1
        else: #처리 불가능
            lt = mid + 1
            
    return answer