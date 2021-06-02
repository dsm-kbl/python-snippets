title = "Meaning " 'of' " Life"

print(title)

print('knight\'s')
print("knight\"s")

print(len('a\nb\tc'))
print('here \a is')

"""
    print(dasdasdas)
"""
#print("abc" + 9)

myjob = "hacker"

for c in myjob:
    print(c, end=' ')

print("k" in myjob)

s = "123456789"
print(s[8:0:-2])
print(repr('spam'))

s = s + 'spam'
print(s)
result = s.find('spam')
print(result)

S = "xxxxSPAMxxxxSPAMxxxx"
replace_all = S.replace('SPAM', 'EGGS')
print(replace_all)
replace_one = S.replace('SPAM', 'EGGS', 1)
print(replace_one)

# String formatting
print('That is %d %s bird' % (1, 'dead'))
# Dictionary based formatting
print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

food = 'spam'
qty = 10
print(vars())

print('%(qty)d more %(food)s' % vars())
