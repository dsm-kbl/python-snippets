##########################################################
import re
S = 'A\nB\tC'  # Each stand for one char

print(len(S))
##########################################################
print(ord('\n'))  # \n is a byte with the binary value 10 in ASCII
##########################################################

msg = """
bbb'''bbbbbbbbbb""bbbbbbb'bbbb
ccccccccccccc
"""
print(msg)

##########################################################
a = "spam".encode('utf-8')
print(a)

b = "spam".encode('utf-16')
print(b)
##########################################################
print('x' + b'y'.decode())
print('x'.encode() + b'y')
##########################################################
# Pattern Matching
match = re.match('Hello[ \t]*(.*)world', 'Hello  Python world')
print(match.group(1))
