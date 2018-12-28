# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of
# mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who
# sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the
# number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

file_name = 'mbox-short.txt'
file_handle = open(file_name)

froms = dict()
# get all of the "from" addresses and their count
for line in file_handle:
    if line.startswith('From '):
        from_address = line.strip().split()[1]
        # Add one to the value matching the key 'from_address' or create the k/v pair if one is not found.
        froms[from_address] = froms.get(from_address, 0) + 1

# find the from address with the highest occurrence
bigaddr = None
bigcount = None
for addr, count in froms.items():
    if bigcount is None or bigcount < count:
        bigaddr = addr
        bigcount = count

print(bigaddr, bigcount)