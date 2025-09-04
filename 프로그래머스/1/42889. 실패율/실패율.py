def solution(N, stages):
    
    answer = []
    stay = [0]*(N+2) #1~N+1까지 쓰려고
    reached = [0]*(N+2)
    # 1단계 스테이지에 도달했으나 클리어 못한 플레이어 수 체크
    for stage in stages:
        stay[stage] += 1
        
    # 스테이지에 도달한 플레이어 수 체크
    reached[N] = stay[N] + stay[N+1]
    #N까지 도달한 사람 = N에서 클리어 x 사람 + N+1 클리어 x 사람
    for i in range(N-1, 0, -1):
    #N부터 1까지 역순(-1)으로 돌겠다        
        reached[i] = stay[i] + reached[i+1]
    # 그리고 그걸 나눠서 실패율 계산
    for i in range(1, N+1):
        if reached[i] == 0:
            fail = 0
        else:
            fail = stay[i] / reached[i]
        answer.append((fail,i)) #실패율, 스테이지 번호 튜플로 저장
    #실패율 내림차순, 스테이지 번호 오름차순
    answer.sort(key=lambda x: (-x[0], x[1]))
    return [stage for _, stage in answer]