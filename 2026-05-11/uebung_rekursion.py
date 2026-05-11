def fakt_iter(n):
    x = 1
    i = 2
    while i <= n:
        x *= i
        i += 1
    return x

def fakt_rek(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * fakt_rek(n-1)

print("Fakultät iterativ:")
n = int(input())
print(f"{n}! = {fakt_iter(n)}")

print("Fakultät rekursiv:")
n = int(input())
print(f"{n}! = {fakt_rek(n)}")