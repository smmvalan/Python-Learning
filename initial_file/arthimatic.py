# swap two integernumber
"""
def swapNumber (firstNumber, secondNumber) :
     temp=firstNumber
    firstNumber=secondNumber
    temp=secondNumber

def main () :
    firstNumber = int (input("Enter the first number"))
    secondNumber = int (input("Enter the second number"))
    print (" the value of first Number before swapping: ", firstNumber)
    print ("the value of second Number before swapping: ", secondNumber)
    return temp, firstNumber

    print(" first number {} and second number {}".format(temp,firstNumber,secondNumber))

    main()

"""

num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)