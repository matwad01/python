file = open("example.txt", 'r')
content = file.read()
print(content)

type(content)

content = file.readlines()
>>> print(content)

>>> file.seek(0)

content = file.readlines()
print(content)
['Line 1\n', 'Line 2\n', 'Line 3\n']
content
['Line 1\n', 'Line 2\n', 'Line 3\n']
content = [i.rstrip("\n") for i in content]
content
['Line 1', 'Line 2', 'Line 3']
