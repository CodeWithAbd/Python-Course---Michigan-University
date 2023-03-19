# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
# filename = input("Enter a file name: ")
# try:
#     with open(filename, 'r') as file:
#         count = 0
#         total = 0
#         for line in file:
#             if line.startswith("X-DSPAM-Confidence:"):
#                 count += 1
#                 confidence = float(line[line.find(":")+1:].strip())
#                 total += confidence
#         average = total / count
#         print("Average spam confidence:", average)
# except FileNotFoundError:
#     print("File not found")


filename = input("Enter a file name:\n")

fh = open(filename, 'r')
count = 0
total = 0
for x in fh:
    if x.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        confidence = float(x[x.find(":")+1:].strip())
        total = total + confidence
average = total / count
print("Average spam confidence:", average)
