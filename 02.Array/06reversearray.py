def reverse_array(arr):
    return arr[::-1]
arr=list(map(int,input().split()))
print(*reverse_array(arr))