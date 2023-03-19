# Dictionaries


# purse = dict()

# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75

# print(purse)
# print(purse['candy'])

# purse['candy'] = purse['candy'] + 2 
# print(purse)


# Dictionaries are like lists except that they use keys instead of numbers to look up values

# Histogram Logic
counts = dict()
names = ['abd', 'adam', 'abd', 'ahsham', 'abd', 'adam', 'abd', 'Abdul rehman']

for x in names:
    if x not in counts:
        counts[x] = 1
    else:
        counts[x] = counts[x] + 1

print(counts)

print("\n")
print("\n")


# The Pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so commomn that there is a method called get() that  does this  for us
c = dict()
for y in names:
    c[y] = c.get(y, 0) + 1
print(c)


# Dictionary and Files

# The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently

stuff = dict()
print(stuff.get('candy',-1))


stuff = dict()
print(stuff['candy'])