fname = input('Enter the file name: ')
fhand = open(fname)
inp = fhand.read()
new_fhand = inp.upper()
print(new_fhand)