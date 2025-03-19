class mex:
    def __init__(self,a):
        self.s=set()
        self.h=[]
        self.c=Counter(a)
        for i in range(n+1):
            if i not in self.c:
                self.s.add(i)
                heappush(self.h,i)
    def add(self,v):
        if v>=n:return
        self.s.discard(v)
        self.c[v]+=1

    def sub(self,v):
        if v>=n:return
        self.c[v]-=1
        if self.c[v]==0:
            self.s.add(v)
            del self.c[v]
            heappush(self.h,v)
    def val(self):
        h=self.h
        while h and h[0]not in self.s:
            heappop(h)
        return h[0]
