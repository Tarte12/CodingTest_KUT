def solution(numbers):
    answer = 0
    lst_num = list(range(10)) 
    for i in numbers:
        if i in lst_num:
            lst_num.remove(i) #pop(i)는 인덱스 기준 제거
    for i in lst_num:
        answer += i
    return answer