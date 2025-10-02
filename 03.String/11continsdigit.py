def contains_all_digits(s):
    try:
        t=int(s)
    except Exception:
        return False
    return True
s=input()
print(contains_all_digits(s))