def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


n=int(input())
m=int(input())
print(gcd(n, m))
print(lcm(n, m))