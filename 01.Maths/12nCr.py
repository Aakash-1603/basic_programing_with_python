import math
def ncr(n,r):
    return math.comb(n,r)
n,r=map(int,input().split())
print(ncr(n,r))