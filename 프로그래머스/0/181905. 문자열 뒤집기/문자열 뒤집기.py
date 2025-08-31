def solution(my_string, s, e):
    slicing = my_string[s:e+1]
    reverse_slicing = slicing[::-1]
    answer = my_string[:s] + reverse_slicing + my_string[e+1:]
    return answer