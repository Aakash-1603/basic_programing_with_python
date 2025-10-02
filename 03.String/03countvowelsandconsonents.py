def vowel(s):
    cnt=0
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            cnt+=1
    return cnt 
def consonents(s):
    cnt=0
    for i in s:
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and i!='A' and i!='E' and i!='I' and i!='O' and i!='U':
            cnt+=1
    return cnt
s=input()
print("Vowels : ",vowel(s))
print("Consonents : ",consonents(s))