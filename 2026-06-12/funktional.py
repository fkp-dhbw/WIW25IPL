## Lambda Funktionen

# kassisch
def quad(x):
    return x*x

quad2 = lambda x: x*x
# Vorteil kompakt, aber vor allem inline

print(quad(5))
print(quad2(5))

zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x*x, zahlen))
print(quadrate)

## List Comprehension
quadrate = [x*x for x in zahlen]
# typisch mathematische Schreibweise, aber auch kompakt
print(quadrate)

gefilterte_quadrate = [x*x for x in zahlen if x % 2 == 0]
print(gefilterte_quadrate)
# Bedingungen, also Filter möglich