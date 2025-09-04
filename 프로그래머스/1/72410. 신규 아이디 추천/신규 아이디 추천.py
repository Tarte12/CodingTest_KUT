def solution(new_id):
    level2 = []
    isTrue = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    level3 = []
    level4 = []
    level5 = []
    level6 = []
    level7 = []
    #1단계: 대문자 -> 소문자
    level1 = new_id.lower()
    #2단계: 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 아닌 문자 제거
    # for문으로 돌면서 new_id.pop 불가능 (문자열 불변)
    for word in level1:
        if word in isTrue:
            level2.append(word)
        # isdigit/isdecimal/isnumeric의 속도 차이는 없는가?
        # idsigit는 유니코드도 True를 반환해서 
        # int만 True로 판단하는 isdecimal로 바꿈
        # 조건문으로 안 하고 허용 함수로 하는 게 성능 차이가 더 좋을까?
    #3단계: 마침표가 연속 => 제거
    for word in level2:
        if len(level3) == 0:
            level3.append(word)
        elif not word == '.':
            level3.append(word)
        else:
            if level3[-1] == '.':
                continue
            else:
                level3.append(word)
    #4단계: 앞뒤 마침표 제거
    level4 = level3
    if level3 and level3[0] == '.':
        # level3이 비면 false로 넘어가 버림
        level4 = level3[1:]
    if level3 and level3[-1] == '.':
        level4 = level4[:-1]
    #5단계: 빈 문자열일 경우 a 대입
    if len(level4) == 0:
        level5.append('a')
    else:
        level5 = level4
    #6단계: 길이 15자 이상이면 15자까지만 출력
    level6 = level5
    if len(level6) > 15:
        level6 = level6[:15]
        if level6[-1] == '.':
            level6 = level6[:-1]
    #7단계: 길이가 2자 이하면 3될 때까지 반복
    if len(level6) < 3:
        num = level6[-1]
        level7 = level6
        while len(level7) < 3:
            level7.append(num)
    else:
        level7 = level6
    level7 = "".join(level7)
    return level7