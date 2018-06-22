#!/bin/python3

def getWays(n, c):
    
    table=[0 for x in range(n+1)]
    table[0]=1
    m=len(c)
    for i in range(0,m):
        for j in range(c[i],n+1):
            table[j]+=table[j-c[i]]
    return table[n]
        

if __name__ == '__main__':

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)
    print(ways)

