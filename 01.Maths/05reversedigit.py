n=int(input())
t=n
# 1st method--
print(int(str(n)[::-1]))

# 2nd method--
ans=0
while t!=0:
    ans*=10
    ans+=t%10
    t//=10
print(ans)
