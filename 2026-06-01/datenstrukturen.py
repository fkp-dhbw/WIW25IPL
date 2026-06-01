## Refenzierungsproblem

int1 = 1
int2 = int1
print(int1, int2)
int2 += 1
print(int1, int2)
# funktioniert wie erwartet

list1 = [4, 7, 1, 1]
list2 = list1
print(list1, list2)
for n in list2:
    n += 1
    # hat gar keine Auswirkung; n ist nur eine Kopie des Werts
print(list1, list2)
for i in range(len(list2)):
    list2[i] += 1
    # verändert die Werte beider Listen
print(list1, list2)

list2 = list1.copy()
for i in range(len(list2)):
    list2[i] += 1
    # hat den gewünschten Effekt
print(list1, list2)

def print_int_plus_1(x):
    x += 1
    print(x)
print(int1)
print_int_plus_1(int1)
print(int1)
# print_int_plus_1 verändert int1 nicht

def print_list_plus_1(x):
    for i in range(len(x)):
        x[i] += 1
    print(x)
print(list1)
print_list_plus_1(list1)
print(list1)
# print_list_plus_1 verändert list1

## Mehrdimensionalität
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Übung Mehrdimensionalität:")
sum = 0
for row in matrix:
  for i in range(len(row)):
    row[i] *= 5
    sum += row[i]
  print(row)
print("Summe aller Elemente der Matrix:", sum)

matrix_new = []
for row in matrix:
  new_row = [0, 0]
  for i in range(len(row)):
    new_row[i//2] += row[i]
  matrix_new.append(new_row)
for row in matrix_new:
  print(row)



print(id(matrix))
matrix2 = matrix
print(id(matrix), id(matrix2))
matrix2 = matrix.copy()
print(id(matrix), id(matrix2))

print(id(matrix[0]), id(matrix2[0]))
# copy erzeugt nur eine flache Kopie, die inneren Listen werden nicht kopiert
import copy
matrix2 = copy.deepcopy(matrix)
print(id(matrix), id(matrix2))
print(id(matrix[0]), id(matrix2[0]))