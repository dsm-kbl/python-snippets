# f = open('data.txt', 'w')
# f.write('Hello\n')
# f.write('world\n')

# f.close()

f = open('data.txt')
text = f.read()
print(text)

print(text.split())
