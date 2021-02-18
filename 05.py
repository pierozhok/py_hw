str = input('введите строку:')
tmp = str.split(' ')
res = []
for s in tmp:
    res.append(int(s))
res.sort()
if res[0]==1:
    for i in range(1, max(res)):
        if i not in res:
            print(i)
            break
else:
    print(1)
