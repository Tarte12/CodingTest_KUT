def solution(answers):
    pattern_1st = [1, 2, 3, 4, 5]
    pattern_2nd = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3rd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    an_1st = (pattern_1st * ((len(answers) // len(pattern_1st)) + 1))[:len(answers)]
    an_2nd = (pattern_2nd * ((len(answers) // len(pattern_2nd)) + 1))[:len(answers)]
    an_3rd = (pattern_3rd * ((len(answers) // len(pattern_3rd)) + 1))[:len(answers)]

    one_count = 0
    two_count = 0
    thr_count = 0

    for idx in range(len(answers)):
        if an_1st[idx] == answers[idx]:
            one_count += 1
        if an_2nd[idx] == answers[idx]:
            two_count += 1
        if an_3rd[idx] == answers[idx]:
            thr_count += 1

    max_count = max(one_count, two_count, thr_count)
    answer = []

    if max_count == one_count:
        answer.append(1)
    if max_count == two_count:
        answer.append(2)
    if max_count == thr_count:
        answer.append(3)

    return answer
