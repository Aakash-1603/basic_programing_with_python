def binary_search(target,arr):
    l=0
    r=len(arr)-1
    while l<=r:
        mid= l+(r-l)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
target=int(input())
arr=list(map(int,input().split()))
print(binary_search(target,arr))