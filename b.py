from math import factorial as fact
def b(n):
    bb=0.5
    i=1
    while n>=i:
        yield bb
        bb=bb/fact(i+2)
        i+=1
    return
if __name__=="__main__":
    n=int(input("n: "))
    for i in b(n, x):
        print(i)