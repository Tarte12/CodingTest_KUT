import sys

# 입력 속도 최적화
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    commands = input().strip()
    left = []
    right = []
    
    for cmd in commands:
        if cmd == '<':
            if left:
                right.append(left.pop())
        elif cmd == '>':
            if right:
                left.append(right.pop())
        elif cmd == '-':
            if left: # 이 체크가 없으면 비어있을 때 에러 발생!
                left.pop()
        else:
            left.append(cmd)
            
    # 정답 출력: left는 정방향, right는 역순이므로 뒤집어서 합침
    print("".join(left) + "".join(reversed(right)))