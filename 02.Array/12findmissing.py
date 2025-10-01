def misssing_number(n,arr):
    return n*(n+1)//2 - sum(arr)
n=int(input())
arr=list(map(int,input().split()))
print(misssing_number(n,arr))