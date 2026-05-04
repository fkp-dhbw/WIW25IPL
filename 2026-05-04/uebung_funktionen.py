def value(x):
    f = x**2 - 2*x + 1 
    print(str(x) + "\t" + str(f)) 

def value_table():
    print("x\tf(x)") 
    print("------------") 
    x = 0 
    while x <= 10:
        value(x)
        x += 1 

value_table()