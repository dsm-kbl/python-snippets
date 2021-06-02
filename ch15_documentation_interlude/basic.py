import sys

print(dir(sys))

print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.startswith('__')]))

print(len([x for x in dir(sys) if not x[0] == '_']))

print(dir([]))
print(dir(''))

print(len(dir([])), len([x for x in dir([]) if not x.startswith('__')]))
print(len(dir('')), len([x for x in dir('') if not x.startswith('__')]))

print([x for x in dir(list) if not x.startswith('__')])
print([x for x in dir(dict) if not x.startswith('__')])

