import string

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
alphabet = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            count += 1
            if letter not in alphabet:
                alphabet[letter] = 1
            else:
                alphabet[letter] += 1

lst = list()
for key, val in list(alphabet.items()):
    lst.append((val, key))
    
lst.sort(reverse=True)
    
for key, val in lst:
    print(key, val)