    def bridges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def union(x,y):
            rx,ry=find(x),find(y)
            if rx==ry:
                return False
            if rank[rx]<rank[ry]:
                rx,ry=ry,rx
            dad[ry]=rx
            rank[rx]+=rank[rx]==rank[ry]
            return True
        def find(x):
            if dad[x]!=x:
                dad[x]=find(dad[x])
            return dad[x]
        G=[[]for _ in range(n)]
        D=[[]for _ in range(n)]
        m=len(edges)
        dad=[*range(n)]
        rank=[0]*n
        for i in range(m):
            u,v=edges[i]
            if union(u,v):
                G[u].append(v)
                G[v].append(u)
            else:
                D[u].append(v)
                D[v].append(u)

        nd=[1]*n
        par=[-1]*n
        idx=[0]*n
        L=[inf]*n
        H=[-inf]*n

        sta=[(0,0)]
        par[0]=0
        preord=[]
        while sta:
            x,lx=sta.pop()
            preord+=[x]
            for v in G[x]:
                if v!=lx:
                    sta.append((v,x))
                    par[v]=x
        for i,e in enumerate(preord):
            idx[e]=i
        for x in preord[::-1][:-1]:
            nd[par[x]]+=nd[x]
    
        for x in preord[::-1]:
            L[x]=min(L[x],idx[x])
            H[x]=max(H[x],idx[x])
            for v in D[x]:
                L[x]=min(L[x],idx[v])
                H[x]=max(H[x],idx[v])
            px=par[x]
            if px==x:continue
            L[px]=min(L[px],L[x])
            H[px]=max(H[px],H[x])
        bridges=[]
        for e in range(1,n):
            if L[e]==idx[e]and H[e]<idx[e]+nd[e]:
                bridges.append((e,par[e]))
        return bridges
