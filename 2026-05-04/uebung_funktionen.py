def calc(x):
  return x**2 - 2*x + 1

def format(x, f): 
  return str(x) + "\t" + str(f)
  #return f"{x}\t{f}"

def value_table():
    print("x\tf(x)") 
    print("------------") 
    x = 0 
    while x <= 10:
        f = calc(x)
        str = format(x, f)
        print(str)
        #print(format(x, calc(x)))
        x += 1 

value_table()