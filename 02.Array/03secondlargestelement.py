def find_second_largest_element(arr):
    if len(arr)<2:
        return 0
    arr.sort(reverse=True)
    return arr[1]
arr=list(map(int,input().split()))
print(find_second_largest_element(arr))