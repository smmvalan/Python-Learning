# To Find out given number is prime or not
# input
givenNumber=int(input("Enter the number:"))
# Process
if givenNumber > 1 :
 if givenNumber==2 :
            print ("This is prime number")    
          
 for i in range (2, givenNumber):
    if (givenNumber % i) == 0 :
            print (givenNumber,"is not a prime number")
            break
    else:
            print(givenNumber, "is a prime number")  
else:  
    print(givenNumber,"is not a prime number")            

