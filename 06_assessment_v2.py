# Component six, puts options in random order

import time

import re

print(type(type(int)))

L = ['a','b','c','d']

print("".join(L))

print(chr(ord('A')))

y = 8
z = lambda x: x * y
print(z(6))

sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())

list1 = [3, 4, 5, 20, 5, 25, 1, 3]
print(list1)
list2 = [3, 4, 5, 20, 5, 25, 1, 3].pop(1)
print(list2)

print(time.time())
print(time.gmtime())
print(time.localtime())
