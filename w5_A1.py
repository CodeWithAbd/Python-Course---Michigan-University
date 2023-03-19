fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
# read the file
fh = open(fname)
counts = dict()
# loop through each line of the file
for line in fh:
    # find lines that start with 'From '
    if line.startswith('From '):
        # split the line into words
        words = line.split()
        # get the sender's email address (second word)
        email = words[1]
        # add the email address to the dictionary, or update the count if it's already in the dictionary
        counts[email] = counts.get(email, 0) + 1
# find the most prolific committer
max_count = None
max_email = None
for email, count in counts.items():
    if max_count is None or count > max_count:
        max_count = count
        max_email = email
print(max_email, max_count)

# Copied. Do it again.