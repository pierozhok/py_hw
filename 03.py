str = input('введите строку:')
str = str.lower()
lst = set(str.split(' '))
cnt = 0
res = {}
for s in lst:
    if (str.count(s) > cnt):
        cnt = str.count(s)
for s in lst:
    if (str.count(s) == cnt):
        res[s]=cnt
print(res)
