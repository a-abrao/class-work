count = 0
total = 0.0
while True:
        line = input('Enter a number: ')
        if line == 'done':
            break
        try:
            value = float(line)
        except:
            print('Error')
            continue
        count = count + 1
        total = total + value
        
print('Total, Sum, and Mean: ')
print(total, count, total/count)