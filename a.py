def a(n, x):
    aa=x
    i=2
    yield aa
    while n>=i:
        aa=aa*x*(i-1)/i
        yield aa
        i+=1
    return
if __name__=="__main__":
    n=int(input("n: "))
    x=int(input("x: "))
    for i in a(n, x):
        print(i)
