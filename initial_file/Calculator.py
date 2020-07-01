# To Find out given number is prime or not
# input
print ("Select Calculator Functions")
print ("Addition: Press 1, Substraction: Press 2, Multiply:3, Divide:4")
userChoice=input (" Enter the choice of operation : ")

num1=int(input("Enter the first number : "))
num2= int (input("Enter the 2nd Number :"))
Add = num1 + num2
Sub = num1 - num2
Mult = num1 * num2
Div = num1/num2
if (userChoice == '1') :
 print ("Addition of Numbers = ", Add) 
elif userChoice == '2' :
 print ("Substract the number",Sub)
elif ( userChoice == '3') :
     print ("Multiplication of Number" , Mult)   
elif ( userChoice == '4') :
  print ("Divide the number", Div)