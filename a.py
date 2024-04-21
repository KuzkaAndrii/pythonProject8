def a(n, x):
    aa=x
    i=1
    while n>=i:
        yield aa
        aa=aa*x*(n-1)/n
        i+=1
    return
if __name__=="__main__":
    n=int(input("n: "))
    x=int(input("x: "))
    for i in a(n, x):
        print(i)