T = (1, 2, 3, 4)  # A 4 item tuple
print(len(T))

print(T + (5, 6))
print(T)

print(T[0])

print(T.index(4))
print(T.count(4))

T = 'spam', 3.0, [11, 22, 33]
print(T)

event = {}

try:
    print(x)
except Exception as e:
    event['exception'] = e

print('test')
print(event['exception'])
