#function 1

def GetUserInput ():
    list1=[]
    colorCount = int(input("Enter the colour list length:"))
    print("Enter the colours one by one:")
    for i in range(colorCount): #3 (0,1,2)
        data=str(input())
        list1.append(data)
    return list1

def AddColors(x, colorName):
     # verify x is list
     x.append(colorName)

def PrintColor(x1):
    for color in x1:
        print(color)

def main():
    #color_list=["red","blue","green","yellow"]
    color_list = GetUserInput()
    AddColors(color_list, "black")
    AddColors(color_list, 'kkk')
    PrintColor(color_list)

main()

''' strg='*'*30
print(strg)

# Function 2 callout list as input

def colorDisplay2 ():
    return
def main():
    list1=[]
    colorCount = int(input("Enter the colour list length:"))
    print("Enter the colours one by one:")
    for i in range(colorCount): #3 (0,1,2)
        data=str(input())
        list1.append(data)
    print(list1)
    print("First Element is {}\nLast Element is {}".format(list1[1],list1[-1]))
    colorDisplay2()
main()
strg='*'*30
print(strg)

# list is a set of codes, collection of instructions

def fun1():
    print('Ryan is tall')
    print('Ryan is year8')
print ('We are living in Fairfield') # this is outside of function
fun1()
strg='*'*30
print(strg)

# Simple Function code
def fun1():
    print('Ryan is tall')
    print('Ryan is year8')
def main():
    print ('We are living in Fairfield') # this is outside of function
    fun1()
main()
print(strg)

# function with mapping

def funct2(num):  # num is an arguments or input values
    print(num)
    return 2*num
def main():
    num=int(input("Enter the number"))
    a=funct2(num)     # return the input value
    print(a)
main()
strg='*'*30
print(strg)
# argument with return values
def funct3(x,y):
    return x+y
a= funct3(5,10)
print(a)
strg='*'*30
print(strg)

# function with multiplication with return value
def fun4(x,y):
    return x*y
def main():
    x=int(input("Enter the first Value"))
    y=int(input("Enter the second value"))
    a=fun4(x,y)
    print(a)
main()
strg='*'*30
print(strg)

'''