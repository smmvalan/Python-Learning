
def average ():
    total = 0
    count = 0

    while True :
        inp = float(input('Enter a number: '))
        if inp == 'done' :
            break
        value = inp
        total = total + value     
        count = count + 1

    avg = total / count
    print ("Average {}\nCount {}".format(avg,count))

def main():     
    average()
    
main()
