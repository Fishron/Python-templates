
class LazySegmentTree:
    def __init__(self, data, default=(0,0,0), func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i<<1], self.data[i<<1|1])

    def __len__(self):
        return self._len

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[idx<<1], self.data[idx<<1|1])
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start + self._size
        stop = stop + self._size
        cr=cl=False
        while start < stop:
            if cl:
                sp=start-1
                self.data[sp]=self._func(self.data[sp<<1],self.data[sp<<1|1])
            if cr:
                self.data[stop]=self._func(self.data[stop<<1],self.data[stop<<1|1])
            if start & 1:
                self.data[start] = tadd(self.data[start],value)
                start += 1
                cl=True
            if stop & 1:
                stop -= 1
                self.data[stop] = tadd(self.data[stop],value)
                cr=True
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        start-=1
        while stop>0:
            if cl:
                self.data[start]=self._func(self.data[start<<1],self.data[start<<1|1])
            if cr and (not cl or start!=stop):
                self.data[stop]=self._func(self.data[stop<<1],self.data[stop<<1|1])

            start>>=1
            stop>>=1
    def query(self, start, stop, default=(0,0,0)):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)
def tadd(x,y):
    return (x[0]+y[0],x[1]+y[1],x[2]+y[2])
def tsub(x,y):
    return (x[0]-y[0],x[1]-y[1],x[2]-y[2])
def LNDS(nums):
    n=len(nums)
    sn=sorted(nums)
    occ=defaultdict(lambda:deque())
    for i,e in enumerate(sn):
        occ[e].append(i)
    
    nn=[0]*n
    #for LNDS
    """for i,e in enumerate(nums):
        nn[i]=occ[e].popleft()"""
    #for LIS
    for i,e in enumerate(nums):
        nn[i]=occ[e][0]
        
    d=[(0,0,0)for i in range(n+1)]
    st=LazySegmentTree(d)
    for i in range(n):
        e=nn[i]
        if i==0:
            d[e]=(1,i,-1)
            st.add(e,e+1,(1,i,-1))
        else:
            od=d[e]
            nv,ni,_=st.query(0,e)
            d[e]=(nv+1,i,ni)
            st.add(e,e+1,tsub(d[e],od))
    v=max(d)
    path=[]
    while 1:
        path+=[v[1]]
        if v[0]==1:break
        v=d[nn[v[2]]]
    return [sn[nn[i]] for i in path]
nums=[1,1,2,4,5,2,2,1,3,1,6,2,7,9,7]
print(LNDS(nums))
