str = input('введите строку:')
res = ''
for s in str:
    if s.isdigit():
        res += s
    else:
        if res.endswith(' '):
            pass
        else:
            res += ' '
sum = 0
lst = res.split(' ')
for s in lst:
    sum += int(s)
print(sum)
