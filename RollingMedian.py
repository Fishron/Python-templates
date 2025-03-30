class RollingMedian():
    def __init__(self):
        self.hm=[]
        self.hM=[]
        self.sm={}
        self.sM={}
        self.sumUnder=0
        self.sumOver=0 #over and equal
    def _filter(self):
        hm,hM,sm,sM=self.hm,self.hM,self.sm,self.sM
        while hM and hM[0][1] not in sM:
            heappop(hM)
        while hm and hm[0][1] not in sm:
            heappop(hm)
    def _transfer(self,d):
        h1,s1,h2,s2=self.hm,self.sm,self.hM,self.sM
        if d:
            h1,s1,h2,s2=h2,s2,h1,s1
        heappush(h2,(-h1[0][0],h1[0][1]))
        del s1[h1[0][1]]
        s2[h1[0][1]] = h1[0][0] * (-1)**d
        
        self.sumOver -= h1[0][0]
        self.sumUnder += h1[0][0]
        heappop(h1)

    def _balance(self):
        hm,hM,sm,sM=self.hm,self.hM,self.sm,self.sM
        while hm and hM and hm[0][0] < -hM[0][0]:
            self._transfer(0)
        while hm and len(sm)>=len(sM)+2:
            self._transfer(0)
        while hM and len(sM)>=len(sm)+1:
            self._transfer(1)

    def clean(self):
        self._filter()
        self._balance()
        self._filter()

    def add(self,el,idx):
        heappush(self.hm,(el,idx))
        self.sm[idx]=el
        self.sumOver+=el
        #self._clean()

    
    def sub(self,idx):
        sm,sM=self.sm,self.sM
        if idx in sm:
            self.sumOver-=sm[idx]
            del sm[idx]
        if idx in sM:
            self.sumUnder-=sM[idx]
            del sM[idx]
        #self._clean() if you want the slightly slower but easier version, you ensure it's clean everytime you write
    def med(self):
        return self.hm[0]

    def __repr__(self):
        self.clean()
        return f"indexes considered in upper (bigger) part {self.sm}\n\
        indexes considered in lower part {self.sM}\n\
        upper part heap {self.hm}\n\
        lower part heap {self.hM}\n\
        upper sum {self.sumOver}\n\
        lower sum {self.sumUnder}\n"
