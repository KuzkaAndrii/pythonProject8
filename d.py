def d(n):
    i=3
    s=4
    a1=0
    a2=1
    if n==1:
        return 0
    elif n==2:
        yield 0
        return 4
    else:
        yield 0
        while n+1>=i:
            yield s
            a2, a1 = a2+i*a1, a2
            s=s+2**i*a2
            i+=1
    return
if __name__=="__main__":
    n=int(input("n: "))
    for i in d(n):
        print(i)