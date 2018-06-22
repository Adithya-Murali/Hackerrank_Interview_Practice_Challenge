

l=list(input())
s=[]
err=0

for x in l:
    if x=='[' or x=='{' or x=='(':
        s.append(x)
    elif x==')':
        p=s.pop()
        if p!='(':
            err=1
            break
    elif x==']':
        p=s.pop()
        if p!='[':
            err=1
            break
    elif x=='}':
        p=s.pop()
        if p!='{':
            err=1
            break

if err==0 and len(s)==0:
    print(True)
else:
    print(False)
