# Data structures are structured variables

# List is a data structure
# A list is a collection meaning in a single variable we can have more than one thing
# List constants are surrounded by square brackets and the elements in the list are separated by commas
# A list element can be any python object - even another list
# A list can be empty

# Eg

print([1,24,76])


# Lists are mutable. Mutable means changeable.
# Strings are immutable - we can not change the contents of a string - we make a new string to make any change.
# Lists are mutable - we can change an element of a list using the index operator

# the Len() function takes a list as a parameter and returns the number of elements in the list. len() tells us the number of elements of any set or sequence
# The range function returns a list.

# Manipulating Lists

a = [1,2,3]
b = [4,5,6]

c = a + b
print(c)


t = [9,41,12,3,4,15]
print(t[1:3])

# b = list()
# print(dir(b))

stuff = list()
stuff.append('book')
stuff.append(101)

print(stuff)
stuff.append('Cookie')
print(stuff)

print('\n')
print('\n')
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

nums = [3,41,12,9,74,15]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

abc = 'With three words'
stuff = abc.split()
print(stuff)

for w in stuff:
    print(w)

# Split breaks a string into parts and produces a list of strings. We think of these as words. WE can access a pirticular word or loop through all the words.

fruit = 'Banana'
print(fruit)
 

z = list(range(5))
print(z)


friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])