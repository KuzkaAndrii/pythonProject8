def c(n):
    cc1=2
    cc2=1
    i=1
    if n==1:
        return cc1
    elif n==2:
        yield cc1
        return cc2
    else:
        yield cc1
        while n >= i:
            yield cc2
            cc2, cc1 =2*cc2-3*cc1, cc2
            i += 1
    return
if __name__=="__main__":
    n=int(input("n: "))
    for i in c(n):
        print(i)