from collections import deque

def solution(arr):
    stack = deque()
    
    for i in arr:
        # if stack: 스택이 비어있지 않을 때
        # stack[-1]: 스택의 마지막 원소
        if not stack or stack[-1] != i:
            stack.append(i)
        
    return list(stack)