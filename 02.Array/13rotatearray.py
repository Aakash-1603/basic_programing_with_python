def rotate_array_by_k_positions(k,arr):
    k%=len(arr)
    return arr[k::]+arr[:-k]
k=int(input())
arr=list(map(int,input().split()))
print(rotate_array_by_k_positions(k,arr))