def test():
    print("Hello")
    return
    # unreachable code
    print("World")

test()

def sub(a, b):
    return a - b

print(sub(5, 2))
print(sub(5, b=3))
print(sub(a=6, b=1))
print(sub(b=4, a=10))

# Default Werte machen einen Parameter optional
# f(x) = ax² + bx + c
def f(x, a=0, b=0, c=0):
    return a*x**2 + b*x + c

print(f(2))
print(f(2, 1, 2, 3))
print(f(2, a=2))
print(f(2, b=3))
test = f(2, a=2, b=3, c=4)
print(test)