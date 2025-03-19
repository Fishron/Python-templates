def sieve(n,func):
    """func must be a 2 arguments multiplicative function which is never 0"""
    #func(p,k)=f(p**k)
    c=[0]*(n+1)
    o=[0]*(n+1)
    spf=[0]*(n+1)
    primes=[]
    for i in range(2,n+1):
        if c[i]==0:
            primes.append(i)
            o[i]=func(i,1)
            c[i]=1
            spf[i]=i
        for p in primes:
            if i*p>n:break
            if p==spf[i]:
                o[i*p]=o[i]//func(p,c[i])*(1+c[i])
                c[i*p]=c[i]+1
                spf[i*p]=p
                break
            else:
                o[i*p]=o[i]*o[p]
                c[i*p]=1
                spf[i*p]=p
    return (primes,o)
