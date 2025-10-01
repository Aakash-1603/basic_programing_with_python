def palin(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
    
n=int(input())
print(palin(n))