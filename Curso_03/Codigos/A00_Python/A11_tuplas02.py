a = (1, 2, [1, 2, 3, 4], 'a', 'b')

print(a)
print(type(a))
print(a.index(2))
print(a.count(2))

a[2].extend([5, 6, 7])
print(a)
