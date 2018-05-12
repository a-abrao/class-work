largest = None
smallest = None
while True:
        line = input('Enter a number: ')
        if line == 'done':
            break
        try:
            value = float(line)
        except:
            print('Error')
            continue
        if largest is None or value > largest:
            largest = value
        if smallest is None or value < smallest:
            smallest = value
        
print('Maximum and Minimum: ')
print(largest, smallest)