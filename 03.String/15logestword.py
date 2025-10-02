def longest_word_in_a_string(s):
    s=s.split()
    length=0
    for i in s:
        length=max(length,len(i))
    return length
s=input()
print(longest_word_in_a_string(s))