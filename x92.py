fname = input('Enter the file name: ')
fhand = open(fname)
weekday = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words [0] != 'From':
        continue
    else:
        if words[2] not in weekday:
            weekday[words[2]] = 1
        else:
            weekday[words[2]] += 1

print(weekday)