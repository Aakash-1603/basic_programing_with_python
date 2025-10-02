def check_anagram(s1,s2):
    return sorted(s1)==sorted(s2)
s1,s2=input().split()
print(check_anagram(s1,s2))