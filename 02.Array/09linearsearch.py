def find_element(target,arr):
    for i in range(len(arr)):
        if target==arr[i]:
            return i
    return -1
target=int(input())
arr=list(map(int,input().split()))
print(find_element(target,arr))