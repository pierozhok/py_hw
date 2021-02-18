while True:
    s = input()
    if s.isdigit():
        if int(s)%2==0:
            print(int(s)/2)
        else:
            print(int(s)*3+1)
    else:
        if s=='cancel':
            print('Bye!')
            break
        else:
            print('Не удалось преобразовать введенный текст в чи
