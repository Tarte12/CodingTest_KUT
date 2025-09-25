from collections import deque
def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    
    ops = 0 
    limit = 3 * (len(q1) + len(q2))
    
    # 두 큐의 합이 같아야 하므로 전체를 더해서 2로 나눈 값이 
    # 두 큐의 합이 될 것
    total = s1 + s2
    target = total // 2
    
    if total % 2 == 1:
        return -1
    
    while s1 != target and ops <= limit:
        if s1 > target:
            if not q1:
                return -1
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
            ops += 1
        else: # s1 < target
            if not q2:
                return -1
            y = q2.popleft()
            q1.append(y)
            s1 += y
            s2 -= y
            ops += 1  
    
    if s1 == target :
        return ops
    else:
        return -1