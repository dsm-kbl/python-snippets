for x in [1, 2, 3, 4]: print(x ** 2, end=' ')
print('\n-----------')
for x in (1, 2, 3, 4): print(x ** 3, end=' ')
print('\n-----------')
for x in 'spam': print(x * 2, end=' ')

# File iterators
print(open('script2.py').read())

for line in open('script2.py'):
    print(line.upper(), end='')

# Iter and next

f = open('script2.py')
print(f.__next__())
print(f.__next__())

g = open('script2.py')
print(next(g))
print(next(g))

L = [1, 2, 3, 4]
I = iter(L)
print(I.__next__())

# Built in Type Iterables
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, D[key])

# List Comprehensions

print([x + 10 for x in [1, 2, 3, 4, 5]])

Z = zip((1, 2, 3), (10, 20, 30))
print(list(Z))

print(list(filter(bool, ['spam', '', 'ni'])))