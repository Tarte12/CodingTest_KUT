import sys

# 빠른 입력을 위한 설정
input = sys.stdin.read

def solve():
    case_num = 1
    input_data = input().split()
    idx = 0

    while True:
        N = int(input_data[idx])
        if N == 0: break
        idx += 1
        
        board = [[0] * 9 for _ in range(9)]
        domino = [[False] * 10 for _ in range(10)]
        row = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        square = [[False] * 10 for _ in range(9)]

        # 도미노 정보 입력
        for _ in range(N):
            n1 = int(input_data[idx]); idx += 1
            p1 = input_data[idx]; idx += 1
            n2 = int(input_data[idx]); idx += 1
            p2 = input_data[idx]; idx += 1
            
            r1, c1 = ord(p1[0]) - ord('A'), int(p1[1]) - 1
            r2, c2 = ord(p2[0]) - ord('A'), int(p2[1]) - 1
            
            board[r1][c1], board[r2][c2] = n1, n2
            domino[n1][n2] = domino[n2][n1] = True
            for r, c, n in [(r1, c1, n1), (r2, c2, n2)]:
                row[r][n] = col[c][n] = square[(r//3)*3 + (c//3)][n] = True

        # 숫자 1~9 위치 입력
        for i, pos in enumerate(input_data[idx:idx+9]):
            r, c = ord(pos[0]) - ord('A'), int(pos[1]) - 1
            board[r][c] = i + 1
            row[r][i+1] = col[c][i+1] = square[(r//3)*3 + (c//3)][i+1] = True
        idx += 9

        def is_possible(r, c, val):
            return not (row[r][val] or col[c][val] or square[(r//3)*3 + (c//3)][val])

        def backtracking(pos):
            if pos == 81:
                return True
            
            r, c = divmod(pos, 9)
            if board[r][c] != 0:
                return backtracking(pos + 1)
            
            for dr, dc in [(0, 1), (1, 0)]: # 가로, 세로 배치
                nr, nc = r + dr, c + dc
                if nr < 9 and nc < 9 and board[nr][nc] == 0:
                    for i in range(1, 10):
                        for j in range(1, 10):
                            if i == j or domino[i][j]: continue
                            if is_possible(r, c, i) and is_possible(nr, nc, j):
                                board[r][c], board[nr][nc] = i, j
                                row[r][i] = col[c][i] = square[(r//3)*3 + (c//3)][i] = True
                                row[nr][j] = col[nc][j] = square[(nr//3)*3 + (nc//3)][j] = True
                                domino[i][j] = domino[j][i] = True
                                
                                if backtracking(pos + 1): return True
                                
                                # 복구 (Backtracking)
                                board[r][c], board[nr][nc] = 0, 0
                                row[r][i] = col[c][i] = square[(r//3)*3 + (c//3)][i] = False
                                row[nr][j] = col[nc][j] = square[(nr//3)*3 + (nc//3)][j] = False
                                domino[i][j] = domino[j][i] = False
            return False

        print(f"Puzzle {case_num}")
        backtracking(0)
        for line in board:
            print("".join(map(str, line)))
        case_num += 1

solve()
