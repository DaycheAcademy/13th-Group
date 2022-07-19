
# Calculate mean of values

counter = 0
sumOfValues = 0
while True:
    inp = input('enter an Integer: ')
    if inp.lower() == 'q' or inp.lower() == 'quit':
        break
    if not inp.isdigit():
        continue
    else:
        sumOfValues = sumOfValues + int(inp)
        counter = counter + 1
meanOfValues = sumOfValues / counter
print(meanOfValues)