def sum_array(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum

def sum_array2(arr):
    return sum(arr)

arr=list(map(int,input().split()))
print(sum_array(arr))
print(sum_array2(arr))