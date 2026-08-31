""" 

"""

a = [[1, 2, 3, 4], ['a', 'b'], ['Pablo', 'Jorge', 'Sara'], [1.2, 3.1416, 8.99]]

print(a[0])
print(a[1])
print(a[2])
print(a[3])

print('Slicing en sublistas')
print(a[2][1:])
a[2].append('Clara')
print(a)
a[3].remove(1.2)
print(a)