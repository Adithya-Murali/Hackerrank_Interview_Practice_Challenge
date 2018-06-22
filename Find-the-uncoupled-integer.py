l=list(map(int,input().split(',')))
s=0
for x in l:
    s=s ^ x
print(s)
