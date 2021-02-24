def fib(n):
    c=2
    n1 = 1
    print(n1)
    n2 = 1
    print(n2)
    while c != n:
        temp = n1 + n2
        n1 = n2
        n2 = temp
        c+=1
        print(n2)
    return
