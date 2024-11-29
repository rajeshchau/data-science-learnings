def sum(*n):
    s=0
    for i in n:
        s +=i
    print(s)
    print(type(n))
    
print(sum(10,20,30,40))