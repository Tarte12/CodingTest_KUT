from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dic = []
    
    # 길이 1~5인 모든 조합 생성
    for len in range(1, 6):
        for comb in product(vowels, repeat=len):
            dic.append(''.join(comb))
    
    dic.sort()
    
    return dic.index(word) + 1