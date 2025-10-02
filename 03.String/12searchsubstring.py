def search_sub_string(s,sub):
    s=s.split()
    for i in s:
        if i==sub:
            return True
    return False
s=input()
sub=input()
print(search_sub_string(s,sub))