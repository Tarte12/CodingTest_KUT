t = int(input()) #테스트 데이터
dic = {
    '(':')'
}
for _ in range(t):
    stack = []
    lst = input()
    valid = True
    for x in lst:
        if x in dic: #여는 괄호
            stack.append(x)
        else: #닫는 괄호
            if not stack: #스택 비었을 때
                valid = False
                break
            open = stack.pop()
            if dic[open] != x: # 스택 맨 위의 값이(여는 괄호)가 x랑 짝이 안 맞을 때
                valid = False
                break

    if valid and not stack:
        print('YES')
    else:
        print('NO')
