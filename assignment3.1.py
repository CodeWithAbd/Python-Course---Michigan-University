
x = int(input("Enter any number\n"))

if x > 5:
    print("Bigger")

if x < 5:
    print("Smaller")

if x == 5:
    print("Equal")


print("\n")
print("\n")
print("\n")
# For Loop
for i in range(5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)

print("All Done")


# Multiway
y = int(input("Enter any number \n"))

if y < 2:
    print("You entered a small number")

elif y < 10:
    print("You entered a medium sized number")

else:
    print("You entered a BIG number")

print("All done")


# Try and Except

# You surround a dangerous section of code with try and except
# If the code in try works - the except is skipped
# If the code in try fails -it jumps to except

sent = 'Hello Bob'

try:
    senti = int(sent)
except:
    senti = -1 

print('First', senti)

print("\n")
print("\n")

num = '123'

try:
    num1 = int(num)
except:
    num1 = -1

print('First', num1)


print("\n")
print("\n")


numbers = input("Enter a number\n")

try:
    val = int(numbers)
except:
    val = -1

if val > 0:
    print("Nice Work")

else:
    print("Not a number")