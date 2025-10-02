def first_non_repeating_character(s):
    dict={}
    for i in s:
        dict[i]=dict.get(i,0)+1
    for i in s:
        if dict[i]==1:
            return i
    return 0
s=input()
print(first_non_repeating_character(s))