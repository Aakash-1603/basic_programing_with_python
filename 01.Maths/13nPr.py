import math
def npr(n,r):
    return math.perm(n,r)
n,r=map(int,input().split())
print(npr(n,r))