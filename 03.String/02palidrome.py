def palindrome(s):
    if s==s[::-1]:
        return True
    return False
s=input()
print(palindrome(s))