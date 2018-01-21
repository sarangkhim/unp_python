while True:
    name = input('당신의 이름은?')
    if name == '종료':
        print('종료합니다.')
        break
    print('{}님, 안녕!'.format(name))