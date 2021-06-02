x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]

a = 0
b = 10
while a < b:
    print(a, end=' ')
    a += 1

def func1():
    ...
def func2():
    ...

func1()
func2()

x = 10
while x:
    x -= 1
    if x%2 != 0: continue
    print(x, end = ' ')


y = 1
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')
