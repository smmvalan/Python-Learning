'''
def maxNum(x,y,z):
    if x>y and x>z:
        return x
    if y>z and y>x:
        return y
    if z>x and z>y:
        return z
def main():
    x = int(input("Enter the 1st numbers: "))
    y = int(input("Enter the 2nd numbers: "))
    z= int(input("Enter the 3rd numbers: "))
    print(max(x,y,z))
    maxNum(x,y,z)
main()
'''

def maxNum(x,y,z):
    if x >=y and x >=z:
        largestNumber = x
    elif y>=z and y>=x:
        largestNumber = y
    else:
        largestNumber = z
    return largestNumber

def main():
    x = int(input("Enter the three numbers: "))
    y = int(input("Enter the three numbers: "))
    z = int(input("Enter the three numbers: "))
    a=maxNum(x,y,z)
    print(a)
    

main()




'''def maxList(list1):
    list1=[20,30,50]
    return max(list1)
'''

    
