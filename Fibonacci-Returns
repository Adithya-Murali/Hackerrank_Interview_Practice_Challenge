table= [0 for x in range(101)]
def dpfib(n):
    if n<=1:
        return n
    
    if table[n-1]==0:
        table[n-1]=dpfib(n-1)
    if table[n-2]==0:
        table[n-2]=dpfib(n-2)
    table[n]=table[n-1]+table[n-2]
    return table[n]

if __name__=='__main__':
    p=[]
    while True:
        try:
            line=int(input())
        except EOFError:
            break
        print(dpfib(line))
