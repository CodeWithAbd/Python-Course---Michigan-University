# Strings

# String is a sequence of characters
# For Strings, + means concatenate
# If a string contains a number, it is still a string
# We can convert numbers in a string into number using int()


fruit = 'banana' #Banana is a six character string
print(len(fruit))
letter = fruit[1]

print(letter)

x = 3 
w = fruit[x - 1]
print(w)


y = len(fruit)
print(y)



index = 0

while index < y:
    letter = fruit[index]
    print(index, letter)
    index = index + 1


for letter in fruit:
    print(letter)
# Letter here is the iteration variable.


# Slicing Strings

# we can also look at any continious section of a string using a colon operator
# The second number is one beyond the end of the slice "up to but not including"
# If the second number is beyond the end of the string, it stops at the end.


# Eg

s = 'Monty Python'

print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])


# String Concatenation

a = 'Hello'
b = a + 'There'

print(b) 
c = a + ' ' + 'There'
print(c)

print('\n')
print('\n')
print('\n')
# The in keyword can also be used to check to see if one string is 'in' another string
# The IN expression is a logical expression that returns True or False and can be used in a n if statement

if('a' in fruit):
    print('Found it\n')


# We can compare strings
# Eg

x = input("Enter a Fruit")
word = x 
if word == 'banana':
    print("All right! Bananas")


pos = fruit.find('na')
print(pos)

# If you get -1 as an output it does not exist.

greet = 'Hello Bob'
rep = greet.replace('Bob', 'Jane')
print(rep)

# Sometimes we want to take a string and remove whitespaces at the beginning or at the end.
# lstrip() and rstrip() remove whitespaces at the left or right
# strip() removes both beginning and ending whitespaces

# We can use find() to find something from a string


x = '40'
y = int(x) + 2
print(y)


# 12 25 28

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
# print(data[pos:pos+3])
print(pos)