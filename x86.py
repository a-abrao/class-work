numlist = []
while True:
        num_inp = input('Enter a number: ')
        if num_inp == 'done':
            break
        try:
            value = float(num_inp)
        except:
            print('Error')
            continue
        
        numlist.append(num_inp)
        
print('Maximum:', max(numlist))
print('Minimum:', min(numlist))