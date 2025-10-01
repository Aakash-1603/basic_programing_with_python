def find_duplicates(arr):
    dict={}
    for i in range(len(arr)):
        dict[arr[i]]=dict.get(arr[i],0)+1
    for num,i in dict.items():
        if i>1:
            return num
    return -1
arr=list(map(int,input().split()))
print(find_duplicates(arr))