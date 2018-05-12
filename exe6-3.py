def count(word, letter):
    count = 0
    for value in word:
        if value == letter:
            count = count + 1
    print(count)