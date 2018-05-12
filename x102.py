fname = input('Enter the file name: ')
fhand = open(fname)
timeofday = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words [0] != 'From':
        continue
    else:
        atpos = words[5].find(':')
        hour = words[5][:atpos]
        if hour not in timeofday:
            timeofday[hour] = 1
        else:
            timeofday[hour] += 1
            
lst = list()
for key, val in list(timeofday.items()):
    lst.append((key, val))
    
lst.sort()
    
for key, val in lst:
    print(key, val)