n=int(input())
if n==1:
    print(0)
if n==2:
    print(0," ",1)
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c