def findfactorial(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
n=int(input())
ans=findfactorial(n)
print(ans)
return 0