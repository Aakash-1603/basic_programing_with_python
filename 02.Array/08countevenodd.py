def count_even(arr):
    cnt=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            cnt+=1
    return cnt
def count_odd(arr):
    cnt=0
    for i in range(len(arr)):
        if arr[i]%2!=0:
            cnt+=1
    return cnt
arr=list(map(int,input().split()))
print(count_even(arr))
print(count_odd(arr))