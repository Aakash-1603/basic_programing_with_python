def arm(n):
    s=str(n)
    l=len(s)
    t=n
    ans=0
    while t!=0:
        digit=t%10
        digit**=l
        ans+=digit
        t//=10
    if ans==n:
        return True
    return False
    
n=int(input())
print(arm(n))