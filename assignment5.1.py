# Loops and Iteration
# Indefinite Loop
n = 5 

while n > 0:
    print(n)
    n = n - 1


print("Blastoff")
print(n)


# Definite Loop

for i in [5,4,3,2,1]:
    print(i)

print('Blastoff')

for i in range(5):
    print(i)

print('Blastoff')


friends = ['Abd', 'abd1', 'bro']
for friend in friends:
    print("Happy New Year", friend)

print('Done')


# Find the largest value

a = [1,45,70,6,8,22,99,1000]

largestNum = -1
print("The largest number is: ", largestNum)
for i in a:
    if i > largestNum:
        largestNum = i
    print(largestNum)

print("The largest number now is: ", largestNum)

print("\n")
print("\n")
print("\n")
# Counting in a loop

y= 0
sum = 0
print("Before", y)

for x in a:
    y = y + 1
    sum = sum + x
    print(y, a, sum)

print("After",y)


n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')



zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)


smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)



