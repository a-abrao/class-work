fname = input('Enter the file name: ')
fhand = open(fname)
email = dict()
maximum = 0

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words [0] != 'From':
        continue
    else:
        if words[1] not in email:
            email[words[1]] = 1
        else:
            email[words[1]] += 1
            
for address in email:
    if email[address] > maximum:
        maximum = email[address]
        max_add = address

print(max_add, maximum)