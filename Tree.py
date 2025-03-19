import sys
from collections import defaultdict,deque,Counter
from heapq import heappush,heappop,heapify
from math import inf,comb,ceil,log,lcm,gcd,isqrt
from functools import cache
from itertools import accumulate,combinations,permutations
from bisect import bisect_left,bisect_right,insort_left
from random import randint

input=lambda:sys.stdin.readline().rstrip()
inp=lambda:list(map(int,input().split()))
I=lambda:int(input())



class SparseTable:
    def __init__(self, data, default=inf, func=min):
        self.default=default
        self.func=func
        n=len(data)
        self.vals=vals=[data]
        i=1
        while 2*i<=n:
            prev=vals[-1]
            vals.append([func(prev[j],prev[j+i]) for j in range(n-2*i+1)])
            i<<=1

    def query(self, start, stop):
        #[start,stop[
        if stop<=start:
            return self.default
        delta=stop-start
        v=delta.bit_length()-1
        return self.func(self.vals[v][start],self.vals[v][stop-(1<<v)])

n=I()
g=[[]for _ in range(n)]
for _ in range(n-1):
    u,v=inp()
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)
depth=[-1]*n
par=[0]*n
nd=[1]*n
layers=[[]for _ in range(n)]
h=[]
idx=[-1]*n
last=[-1]*n
q=[(0,0)]
depth[0]=0
euler=[]
while q:
    d,x=q.pop()
    last[x]=len(euler)
    euler.append(depth[x])
    if d==1:continue
    idx[x]=len(h)
    h.append(x)
    layers[depth[x]].append(x)
    for v in g[x]:
        if depth[v]==-1:
            depth[v]=1+depth[x]
            par[v]=x
            q.append((1,x))
            q.append((0,v))
for e in h[::-1][:-1]:
    nd[par[e]]+=nd[e]
spt=SparseTable(euler)
l=n.bit_length()+1
bl=[[0]*n for _ in range(l)]
for j in range(n):
    bl[0][j]=par[j]
for i in range(1,l):
    for j in range(n):
        bl[i][j]=bl[i-1][bl[i-1][j]]
def lca(x,y):
    if idx[x]<=idx[y]<idx[x]+nd[x]:return x

    for v in range(l-1,-1,-1):
        cand=bl[v][x]
        if not (idx[cand]<=idx[y]<idx[cand]+nd[cand]):
            x=cand
    return par[x]

layers=[e for e in layers if e]

def dist(x,y):
    lx,ly=last[x],last[y]
    if lx>ly:
        lx,ly=ly,lx
    return depth[x]+depth[y]-2*spt.query(lx,ly+1)
