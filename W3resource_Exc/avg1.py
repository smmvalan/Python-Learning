numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : 
        break
    value=int(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print ('Average:', average)
