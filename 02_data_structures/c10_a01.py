# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file_name = 'mbox-short.txt'
file_handle = open(file_name, 'r')
hours = dict()
for line in file_handle:
    # get the line with the data we're looking for
    if line.startswith('From '):
        # split on spaces. get index 5 (timestamp). split on ':'. Get index 0 (hour)
        hour = line.split()[5].split(':')[0]
        # increment occurrence of hour by 1 in dictionary
        hours[hour] = hours.get(hour, 0) + 1

for hour, count in sorted(hours.items()):
    print(hour, count)