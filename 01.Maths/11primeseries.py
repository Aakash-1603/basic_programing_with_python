def prime(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
def prime_number_upto_n(n):
    primes=[]
    for i in range(n):
        if prime(i):
            primes.append(i)
    return primes
n=int(input())
print(*prime_number_upto_n(n))