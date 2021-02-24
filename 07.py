input = open("/etc/passwd",mode = 'r',encoding = 'utf-8')
a = []
res = [[1]]
for line in input1:
    a.append(line.split(':'))
for r in a:
    if r[6][0:5]=='/bin':
        ch = 0
        for i in range(len(res)):
            if r[6] in res[i]:
                ch+=1
        if ch==0:
            res.append([r[6],0])
for r in a:
    for o in range(len(res)):
        if r[6] in res[o]:
            res[o][1]+=1
input.close()
output = open("output1.txt",mode = 'w')   
for r in res:
    output.write(r,'\n')
output.close()

input = open("/etc/group",mode = 'r',encoding = 'utf-8')
a = []
res = []
for line in input2:
    a.append(line.split(':'))
for r in a:
    if r[3] not null:
        res.append([a[0],a[3],[]])
for r in range(len(res)):
    lst = res[r][1].split(',')
    for n in lst:
        for i in a:
            if n==i[0]:
                res[r][2].append(i[2])
input.close()
output = open("output2.txt",mode = 'w')   
for r in res:
    output.write(r[0],r[2],'\n')
output.close()
