txt = "Hello World"
x=txt.replace("H","J")
print(x)

txt = "Hello World"
txt=txt.upper()
print(txt)

txt = "Hello World"
txt=txt.lower()
print(txt)

# Get the first character of the string txt.
txt = "Hello World"
print(txt[0])

# Get the character length of this word
txt = "Hello World"
print(len(txt))
# Get the characters from index 2 to index 4
txt = "Hello World"
print(txt[2:5])
# Return the string without any whitespace at the beginning
txt=       "Hellow World"
print(txt.strip())

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# display datatypes: String, int , float , complex:
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = range(6)
print(x)
x = {"name" : "John", "age" : 36}
print(type(x))
x = True and False
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = b"Hello"
print(type(x))


