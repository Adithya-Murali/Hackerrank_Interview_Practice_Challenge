class node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class ll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert(self,data):
        newn=node(data)
        if self.head is None:
            self.head=newn
            self.tail=newn
        else:
            newn.prev=self.tail
            self.tail.next=newn
            self.tail=newn
        
    def shown(self,key):
        curr=self.tail
        while key>1:
            if curr.prev is None:
                print('NIL')
                return
            curr=curr.prev
            key=key-1
        
        print(curr.data)
        
            
            
if __name__=='__main__':
    obj=ll()
    err=0
    try:
        key=int(input())
        l=list(map(int,input().split()))
    except:
        err=1
    if key<=0 or key>len(l):
        err=1
    if len(l)<=0 or len(l)>=1024:
        err=1
    if err==1:
        print('NIL')
    else:
        for x in l:
            obj.insert(x)
        obj.shown(key)
