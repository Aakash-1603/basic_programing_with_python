def first_method_binary(n):
    return bin(n)[2:]
def second_method_binary(n):
    s=""
    while n!=0:
        s+=str(n%2)
        n//=2
    return s[::-1]
n=int(input())
print(first_method_binary(n))
print(second_method_binary(n))