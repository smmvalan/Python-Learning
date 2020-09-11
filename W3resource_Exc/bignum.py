'''
list1=[]
num=int(input("Enter the elements"))

for i in range (1,num+1):

    ele=int(input("Enter the elements"))
    list1.append(ele)
large=max(list1)
prin

def bigNum(num):
    list1=[]
    
    for i in range (1, num+1):
        ele = int (input("Enter the element"))
        list1.append(ele)
    print(max(list1))
    return 
def main():
    num= int (input("Enter the element"))
    bigNum (num)
main()
t("list of numbers: {}\n largest Number: {}".format(list1,large))
'''
def generateList(numberOfElements):
    'Genrates list based on paramenter'
    list1=[]
    
    for i in range (1, numberOfElements+1):
        ele = int (input("Enter the element"))
        list1.append(ele)

    return list1
def main():
    num= int (input("Enter the element"))
    collectionItem = generateList (num)
    print("list of numbers: {}\n largest Number: {}".format(collectionItem,max(collectionItem)))

main()

