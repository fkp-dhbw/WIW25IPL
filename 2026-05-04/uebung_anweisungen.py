print("Fakultät:")
n = int(input())
x = 1
i = 2
while i <= n:
    x *= i
    i += 1
print(n, "! =", x)

########################

print("Fibonacci:")
n = int(input())
x, x1, x2 = 1, 1, 1
i = 3
while i <= n:
    x = x1 + x2 
    x2 = x1
    x1 = x
    i += 1
print("fib(", n, ")=", x)

########################

print("Fakultät umgekehrt:")
x_ziel = int(input())
n = 1
x = 1
while x < x_ziel:
    n += 1
    x *= n
print(n, "! >=", x_ziel)

########################

print("Fibonacci umgekehrt:")
x_ziel = int(input())
n = 2
n, x, x1, x2 = 1, 1, 1, 0
while x < x_ziel:
    x = x1 + x2
    x2 = x1
    x1 = x
    n += 1
print("fib(", n, ")>=", x_ziel)
