def average(arr):
    return sum(arr)//len(arr)

def mean(arr):
    return sum(arr)//len(arr)

def median(arr):
    if len(arr)%2==0:
        return (arr[len(arr)//2]+arr[len(arr)//2 +1])//2
    else:
        return arr[len(arr)//2]

def mode(arr):
    dict={}
    for i in range(len(arr)):
        dict[arr[i]]=dict.get(arr[i],0)+1
    maxi=max(dict.values())
    for num,cnt in dict.items():
        if cnt==maxi:
            return num

arr=list(map(int,input().split()))
print(average(arr))
print(mean(arr))
print(median(arr))
print(mode(arr))