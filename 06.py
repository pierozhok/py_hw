sum = 45
for i in range(10, 1000000):
    if (str(i)==str(i)[::-1]) and (str(bin(i))[2:]==str(bin(i))[:1:-1]):
        sum += i
print(sum)
