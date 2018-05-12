fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        atpos = line.find(':')
        num = float(line[atpos+1:-1])
        total = total + num
average = total/count
print('Average spam confidence: ', average)