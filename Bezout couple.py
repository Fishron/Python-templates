def bezout(a,b):
    r,u,v=a,1,0
    R,U,V=b,0,1
    while R!=0:
        x=r//R
        r,u,v,R,U,V=R,U,V,r-x*R,u-x*U,v-x*V
    return r,u,v
