def solution(board, moves):
    answer = 0
    stack = [] #바구니
    #열 포인터
    n = len(board) #행 길이 = 가로
    m = len(board[0]) #열 길이 = 세로
    
    nextRow = [n] * m #기본값은 n
    
    for col in range(m): #세로 길이 만큼 돌겠다
        for row in range(n): #가로 길이 만큼 돌겠다
            if board[row][col] != 0: #만약 인형이 있을 경우
                nextRow[col] = row #열 포인터 초기 세팅 값
                break
    #이러고 인형 뽑으면 포인터에 +1 하겠다
    #격자판
    for i in moves: #moves로 인형을 뽑아야 하므로
        col = i-1
        row = nextRow[col]
        if row >= n:
            continue
        doll = board[row][col]
        
        row += 1
        while row < n and board[row][col] == 0:
            row += 1
        nextRow[col] = row

        # 바구니
        if stack and stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)
    
    return answer