from functools import cache
from math import inf

@cache
def f(x,isSnake=0,suffixMax=-inf):
    if x<0:return 0
    if x==0:return isSnake
    return sum(f((x-d)//10,d>suffixMax and suffixMax!=-inf or d==0 and isSnake,max(suffixMax,d))for d in range(10))

l,r=map(int,input().split())

print(f(r)-f(l-1))
