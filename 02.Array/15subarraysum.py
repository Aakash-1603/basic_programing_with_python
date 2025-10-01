def max_subarray_sum(arr):
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far
arr=list(map(int,input().split()))
print(max_subarray_sum(arr))