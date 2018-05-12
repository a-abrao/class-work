fname = input('Enter the file name: ')
fhand = open(fname)
t = list()
for line in fhand:
    for i in line.split():
        if not i in t:
            t.append(i)

t.sort()  
print(t)
    