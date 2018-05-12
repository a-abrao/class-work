fname = input('Enter the file name: ')
fhand = open(fname)
email = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words [0] != 'From':
        continue
    else:
        if words[1] not in email:
            email[words[1]] = 1
        else:
            email[words[1]] += 1

lst = list()
for key, val in list(email.items()):
    lst.append((val, key))
    
lst.sort(reverse=True)
    
for key, val in lst:
    print(key, val)