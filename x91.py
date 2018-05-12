fname = input('Enter the file name: ')
fhand = open(fname)
words = dict()

fwords = fhand.read()
word_dict = fwords.split()
for word in word_dict:
    words[word] = 0