nd=[1]*n
par=[-1]*n
parC=[-1]*n

def centroid(start):
    q=[start]
    par[start]=start
    for e in q:
        for v in g[e]:
            if par[v]==-1 and parC[v]==-1:
                par[v]=e
                q.append(v)
    N=len(q)
    for e in q[::-1][:-1]:
        nd[par[e]]+=nd[e]   
    q2=[start]
    for e in q2:
        for v in g[e]:
            if N//2<nd[v]<nd[e] and parC[v]==-1:
                q2.append(v)
                break
        else:
            for el in q:
                nd[el]=1
                par[el]=-1
            return e

def centroidTree(g):
    cur=0
    root=centroid(0)
    parC[root]=root
    q=[root]
    for e in q:
        for v in g[e]:
            if parC[v]==-1:
                cand=centroid(v)
                parC[cand]=e
                q.append(cand)
    gc=[[]for _ in range(n)]
    for i in range(n):
        pi=parC[i]
        if pi!=i:
            gc[i]+=[pi]
            gc[pi]+=[i]
            
    return gc
