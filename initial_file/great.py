# To show the largest number among three values
'''
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')
num3= input ('Enter the third Number:')
ars = '*'*50
print(" First Number: {} \n Second Number : {}\n Third Number : {}".format(num1,num2,num3))

if num1 > num2 and num1 > num3 :
   largest = num1 
elif num2 > num3 and num2 > num3 :
   largest = num2
else:
    largest = num3
print("the greatest among the number: ", largest)


'''
def swapNumber (num1, num2) :
    'enter the two integer numbers'
    temp = num1  #20
    num1 = num2  #30
    num2 = temp # 20
    return num1 , num2
def main ():
    num1 = int (input ("Enter the first number before swap :"))
    num2 = int (input("Enter the second number before swap :"))
    a,b = swapNumber (num1,num2)
    print ("the number after swapping {}\n {}".format(a,b))

main ()



