while True:
    s = input()
    if s == '#':
        break

    ch, str = s[0], s[2:]   # 첫 글자와 공백 이후의 문장 분리
    str = str.lower()
    ch = ch.lower()

    cnt = str.count(ch)
    print(ch, cnt)
