if 1:
    print('true')


if not 1:
    print('True')
else:
    print('False')

choice = 'ham'
print({
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99,
    'bacon': 1.10
}[choice])

branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
# Setting default if key does not exist
print(branch.get('spam', 'Bad Choice'))

choice = 'bacon'
try:
    print(branch[choice])
except KeyError:
    print('Bad Choice')

x = 1 + 2 + 3 \
    + 4

print(x)

# Ternary Expression
A = 't' if 'spam' else 'f'
print(A)
