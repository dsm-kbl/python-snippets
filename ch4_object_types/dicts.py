# Dictionaries
D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = '40'

print(D)

bob1 = dict(name='Bob1', job='dev', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob2', 'dev', 40]))
print(bob2)

# Nesting
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

print(rec['name'])

rec['jobs'].append('janitor')
print(rec)

# Checkinf for Missing keys
D = {'a': 1, "b": 2, 'c': 3}
print(D)
D['e'] = "99"
if not 'f' in D:
    print('missing')

value = D.get('x', 0)
print(value)

value = D['x'] if 'x' in D else 0
print(value)

keys = list(D.keys())
print(keys)

keys.sort()
print(keys)
for key in keys:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

# Iteration and Optimization
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
