fname = input('Enter the file name: ')
try:
    if fname == "na na boo boo":
            print("You've been punk'd")
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)