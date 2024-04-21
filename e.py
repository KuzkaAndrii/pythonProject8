import math
def gena(x, n):
    a=x
    i=2
    while n>=i:
        yield a
        a = a * (-1.0) * x * x / ((2 * i - 1) * (2 * i - 2))
        i+=1
    return
def sin(x, eps=0.01):
    s = 0.0
    sp = 0.0
    for a in gena(x, 10000000):
        s, sp = s+a, s
    if abs(s-sp)<eps:
        return s

if __name__=="__main__":
    x=float(input("x: "))
    print(math.sin(x))
    print(sin(x, 0.00000001))