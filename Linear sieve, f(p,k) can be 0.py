def sieve(n,func):
    c=[0]*(n+1)
    o=[0]*(n+1)
    o[1]=1
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
                #specific formula for i%p==0
                o[i*p]=0
                c[i*p]=c[i]+1
                spf[i*p]=p
                break
            else:
                o[i*p]=o[i]*o[p]
                c[i*p]=1
                spf[i*p]=p
    return (primes,o)
#example with mobius
def func(p,k):
    return (k==0)-(k==1)
