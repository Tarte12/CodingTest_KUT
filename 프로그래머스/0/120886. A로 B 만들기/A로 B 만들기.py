def solution(before, after):
    
    lst_before = list(before)
    lst_after = list(after)
    for i in lst_before:
        if i in lst_after:
            lst_after.remove(i)
        else:
            return 0
    return 1