def remove_duplicate(s):
    S=[]
    for i in s:
        if i not in S:
            S.append(i)
    res=""
    for i in S:
        res+=i
    return res
s=input()
print(remove_duplicate(s))