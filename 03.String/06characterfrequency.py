def character_frequency(s):
    dict={}
    for i in s:
        dict[i]=dict.get(i,0)+1
    return dict
s=input()
print(character_frequency(s))