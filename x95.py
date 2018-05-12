fname = input('Enter the file name: ')
fhand = open(fname)
domain = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words [0] != 'From':
        continue
    else:
        atpos = words[1].find('@')
        email = words[1][atpos+1:]
        if email not in domain:
            domain[email] = 1
        else:
            domain[email] += 1

print(domain)