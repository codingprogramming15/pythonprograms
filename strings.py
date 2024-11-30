'''
collection of characters
'''

# a='pythonlife'
# b="pythonlife"
# c='''pythonlife'''
# print(type(a),type(b),type(c))

'''
lower
upper
ends with
starts with
replace
find
index
count
remove prefix
remove suffix
split
strip
rstrip
lstrip
'''

# pythonlife='please subscribe'
# print(pythonlife.upper())

# pythonlife='PLEASE SUBSCRIBE'
# print(pythonlife.lower())

# Pythonlife="python language"
# print(Pythonlife.startswith("p"))

# Pythonlife="python language"
# print(Pythonlife.replace("language","programming"))

# Pythonlife="python language"
# print(Pythonlife.index("python"))
# print(Pythonlife.find("python"))

# Pythonlife="python language"
# print(Pythonlife.count('p'))
# print(Pythonlife.removeprefix("python"))
# print(Pythonlife.removesuffix("language"))

# Pythonlife="python language"
# print(Pythonlife.split())
pythonlife="    python  language      "
print(pythonlife)
print(len(pythonlife))
v=pythonlife.strip()
print(len(v))
v=pythonlife.lstrip()
print(len(v))
v=pythonlife.rstrip()
print(len(v))