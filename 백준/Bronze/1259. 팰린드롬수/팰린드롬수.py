while True:
    num = str((input()))
    if num == '0':
        break
    reverse = num[::-1]
    if num == reverse:
        print('yes')
    else:
        print('no')
