def fib(a,b,i,n): 
    c=a+b
    if i==n:
        print(c)
        return
    else:
        a=b
        b=c
        i=i+1
        fib(a,b,i,n)

if __name__=='__main__':
    a=0
    b=1
    n=int(input())
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        fib(a,b,2,n)
