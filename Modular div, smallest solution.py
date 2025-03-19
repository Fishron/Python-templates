def div(a,b,mod):
    #smallest k such that b*k = a (%mod) or inf if no such k exists
    a%=mod
    b%=mod
    gc=gcd(b,mod)
    if a%gc:
        return inf
    b//=gc
    mod//=gc
    a//=gc
    return a*pow(b,-1,mod)%mod
