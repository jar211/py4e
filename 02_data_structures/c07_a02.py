# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those
# values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter
# mbox-short.txt as the file name.

input_file_name = input('Enter a file name: ')
file_handle = open(input_file_name, 'r')
tot = 0.0
count = 0
for line in file_handle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        xpos = line.find(':')
        val = float(line[xpos+1:].strip())
        count = count + 1
        tot = tot + val

print('Average spam confidence:', tot/count)


